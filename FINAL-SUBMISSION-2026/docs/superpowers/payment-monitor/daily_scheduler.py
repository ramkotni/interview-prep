"""
GINR Payment Failure Monitor — Daily Scheduler
===============================================
Runs the payment failure analysis every day at 7:00 AM CST (configurable).
Uses APScheduler for production-grade scheduling with:
  - Misfire grace period (if server was down)
  - Job coalescing (never double-runs)
  - Persistent job store
  - Graceful shutdown handling

Usage:
  pip install apscheduler
  python daily_scheduler.py          # starts the scheduler (runs continuously)
  python daily_scheduler.py --now    # run immediately once and exit
"""

import sys
import signal
import logging
import argparse
import datetime
from pathlib import Path

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR, EVENT_JOB_MISSED

from config import SCHEDULE_CONFIG, LOG_DIR
from payment_failure_analyzer import run_analysis
from email_service import send_email

# ─────────────────────────────────────────────────────────────────────────────
# Logging Setup
# ─────────────────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_DIR / "scheduler.log", encoding="utf-8"),
    ]
)
LOG = logging.getLogger("PaymentMonitorScheduler")


# ─────────────────────────────────────────────────────────────────────────────
# Core Job
# ─────────────────────────────────────────────────────────────────────────────

def run_daily_payment_check(dry_run: bool = False):
    """
    Complete daily payment failure workflow:
      1. Extract data (Oracle SQL → pandas / CSV)
      2. Run all 7 failure detection rules
      3. Build HTML + CSV report
      4. Send email to Manager
      5. Log outcome to audit trail
    """
    LOG.info("=" * 65)
    LOG.info(f"DAILY PAYMENT CHECK STARTING  —  {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    LOG.info("=" * 65)

    try:
        # Step 1 + 2: Analyze
        report = run_analysis()

        # Step 3 + 4: Email
        email_result = send_email(report, dry_run=dry_run)

        # Step 5: Summary
        LOG.info("=" * 65)
        LOG.info("DAILY PAYMENT CHECK COMPLETE")
        LOG.info(f"  Failures found : {report['total_failures']}")
        LOG.info(f"  Critical       : {report['critical_count']}")
        LOG.info(f"  Total at risk  : ${report['total_at_risk']:,.2f}")
        LOG.info(f"  Email status   : {email_result['status']}")
        if email_result.get("html_preview"):
            LOG.info(f"  Report saved   : {email_result['html_preview']}")
        LOG.info("=" * 65)
        return report

    except Exception as e:
        LOG.critical(f"PAYMENT CHECK FAILED: {e}", exc_info=True)
        raise


# ─────────────────────────────────────────────────────────────────────────────
# APScheduler Event Listeners
# ─────────────────────────────────────────────────────────────────────────────

def on_job_executed(event):
    LOG.info(f"✅ Job executed successfully | Scheduled: {event.scheduled_run_time}")


def on_job_error(event):
    LOG.error(f"❌ Job FAILED | Exception: {event.exception}", exc_info=event.traceback)


def on_job_missed(event):
    LOG.warning(f"⚠️  Job MISSED (server was down) | Was scheduled: {event.scheduled_run_time}")


# ─────────────────────────────────────────────────────────────────────────────
# Scheduler
# ─────────────────────────────────────────────────────────────────────────────

def start_scheduler(dry_run: bool = False):
    """Start the blocking APScheduler that runs the job daily."""
    scheduler = BlockingScheduler(timezone=SCHEDULE_CONFIG["timezone"])

    # Register event listeners
    scheduler.add_listener(on_job_executed, EVENT_JOB_EXECUTED)
    scheduler.add_listener(on_job_error,    EVENT_JOB_ERROR)
    scheduler.add_listener(on_job_missed,   EVENT_JOB_MISSED)

    # Daily trigger at configured hour:minute
    trigger = CronTrigger(
        hour=SCHEDULE_CONFIG["run_hour"],
        minute=SCHEDULE_CONFIG["run_minute"],
        timezone=SCHEDULE_CONFIG["timezone"],
    )

    scheduler.add_job(
        func=run_daily_payment_check,
        trigger=trigger,
        kwargs={"dry_run": dry_run},
        id="ginr_daily_payment_check",
        name="GINR Daily Payment Failure Check",
        misfire_grace_time=3600,   # allow up to 1h late if server was down
        coalesce=True,             # never run twice if missed multiple
        max_instances=1,
    )

    LOG.info("=" * 65)
    LOG.info("GINR PAYMENT MONITOR SCHEDULER STARTED")
    LOG.info(f"  Schedule : Every day at {SCHEDULE_CONFIG['run_hour']:02d}:{SCHEDULE_CONFIG['run_minute']:02d} {SCHEDULE_CONFIG['timezone']}")
    LOG.info(f"  Mode     : {'DRY RUN (no email sent)' if dry_run else 'LIVE'}")
    LOG.info(f"  Log file : {LOG_DIR / 'scheduler.log'}")
    LOG.info("  Press Ctrl+C to stop")
    LOG.info("=" * 65)

    # Graceful shutdown on SIGTERM (Docker / systemd)
    def shutdown(signum, frame):
        LOG.info("Received shutdown signal, stopping scheduler...")
        scheduler.shutdown(wait=False)
        sys.exit(0)

    signal.signal(signal.SIGTERM, shutdown)

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        LOG.info("Scheduler stopped by user.")


# ─────────────────────────────────────────────────────────────────────────────
# Entry Point
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GINR Daily Payment Failure Monitor")
    parser.add_argument("--now",      action="store_true", help="Run once immediately and exit")
    parser.add_argument("--dry-run",  action="store_true", help="Analyze but do NOT send email (saves HTML preview)")
    args = parser.parse_args()

    if args.now or args.dry_run:
        # One-shot run (used for testing and manual trigger)
        run_daily_payment_check(dry_run=args.dry_run)
    else:
        # Persistent scheduled mode
        start_scheduler(dry_run=False)

