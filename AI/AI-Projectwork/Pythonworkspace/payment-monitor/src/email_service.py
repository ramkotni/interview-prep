"""
GINR Payment Failure — Email Service
=====================================
Builds a rich HTML email and sends it via SMTP (Office 365 / ERCOT).
Attaches a CSV report for the Manager.

Called by daily_scheduler.py after payment_failure_analyzer.py runs.
"""

import smtplib
import csv
import io
import logging
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path

from config import EMAIL_CONFIG, APP_INFO, REPORT_DIR, OLLAMA_CONFIG

try:
    import ollama
except Exception:
    ollama = None

LOG = logging.getLogger("EmailService")

# ─────────────────────────────────────────────────────────────────────────────
# Severity → HTML badge styles
# ─────────────────────────────────────────────────────────────────────────────
BADGE_STYLE = {
    "CRITICAL": "background:#C0392B;color:#fff;padding:3px 8px;border-radius:4px;font-size:11px;font-weight:bold;",
    "HIGH":     "background:#E67E22;color:#fff;padding:3px 8px;border-radius:4px;font-size:11px;font-weight:bold;",
    "MEDIUM":   "background:#F39C12;color:#fff;padding:3px 8px;border-radius:4px;font-size:11px;font-weight:bold;",
    "LOW":      "background:#27AE60;color:#fff;padding:3px 8px;border-radius:4px;font-size:11px;font-weight:bold;",
}


def _generate_ai_summary(report: dict) -> str:
    """Generate a concise AI executive summary using Ollama when enabled."""
    if not OLLAMA_CONFIG["enabled"]:
        return ""
    if ollama is None:
        LOG.warning("Ollama summary enabled but ollama package is not installed.")
        return ""

    prompt = f"""
You are an ERCOT finance reporting assistant.
Write a concise executive summary for a daily payment failure report.
Do not use markdown.
Keep it to 5-7 bullet-style lines in plain text.

Metrics:
- Total records scanned: {report['total_records']}
- Total failures: {report['total_failures']}
- Critical failures: {report['critical_count']}
- High priority failures: {report['high_count']}
- Total amount at risk: ${report['total_at_risk']:,.2f}

Include:
1) Main risk posture
2) Most urgent issue category
3) Business impact in plain language
4) Immediate next actions for operations team
"""

    try:
        response = ollama.chat(
            model=OLLAMA_CONFIG["model"],
            messages=[{"role": "user", "content": prompt}],
        )
        return response["message"]["content"].strip()
    except Exception as ex:
        LOG.warning(f"Ollama summary generation failed: {ex}")
        return ""


# ─────────────────────────────────────────────────────────────────────────────
# HTML Builder
# ─────────────────────────────────────────────────────────────────────────────

def build_html_email(report: dict) -> str:
    """Build the complete HTML email body from the analysis report."""

    run_date      = report["run_date"]
    total_fail    = report["total_failures"]
    total_risk    = report["total_at_risk"]
    critical      = report["critical_count"]
    high          = report["high_count"]
    summary       = report["summary_by_type"]
    meta          = report["failure_meta"]
    ai_summary    = _generate_ai_summary(report)

    # ── Overall alert banner color ──────────────────────────────────────────
    if critical > 0:
        banner_color, banner_label = "#C0392B", "🔴 CRITICAL ALERT"
    elif high > 0:
        banner_color, banner_label = "#E67E22", "🟠 HIGH PRIORITY"
    elif total_fail > 0:
        banner_color, banner_label = "#F39C12", "🟡 ATTENTION NEEDED"
    else:
        banner_color, banner_label = "#27AE60", "✅ ALL CLEAR"

    # ── Summary cards ────────────────────────────────────────────────────────
    def card(label, value, bg):
        return f"""
        <td style="text-align:center;padding:15px 20px;background:{bg};
                   border-radius:8px;margin:5px;">
          <div style="font-size:28px;font-weight:bold;color:#fff;">{value}</div>
          <div style="font-size:12px;color:#fff;margin-top:4px;">{label}</div>
        </td>"""

    cards_html = f"""
    <table cellpadding="10" cellspacing="10" style="width:100%;border-collapse:separate;">
      <tr>
        {card("Total Failures", total_fail, "#2C3E50")}
        {card("Critical", critical, "#C0392B")}
        {card("High Priority", high, "#E67E22")}
        {card("$ At Risk", f"${total_risk:,.0f}", "#1A5276")}
        {card("Records Scanned", report['total_records'], "#117864")}
      </tr>
    </table>"""

    # ── Section per failure type ─────────────────────────────────────────────
    sections_html = ""
    severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2}

    sorted_types = sorted(
        summary.items(),
        key=lambda x: severity_order.get(x[1]["severity"], 3)
    )

    for ftype, data in sorted_types:
        m         = meta[ftype]
        sev       = m["severity"]
        badge     = f'<span style="{BADGE_STYLE[sev]}">{sev}</span>'
        row_color = {"CRITICAL": "#FDECEA", "HIGH": "#FEF3E2", "MEDIUM": "#FEF9E7"}.get(sev, "#fff")
        records   = data["records"]

        # Build detail rows table
        detail_rows = ""
        for rec in records[:25]:  # cap at 25 per section
            detail_rows += f"""
            <tr style="border-bottom:1px solid #eee;">
              <td style="padding:6px 8px;font-family:monospace;font-size:12px;">{rec.get('ginr_request_id','')}</td>
              <td style="padding:6px 8px;font-size:12px;">{rec.get('inr_id','')}</td>
              <td style="padding:6px 8px;font-size:12px;">{rec.get('company_name','')}</td>
              <td style="padding:6px 8px;font-size:12px;">{rec.get('resource_type','')}</td>
              <td style="padding:6px 8px;font-size:12px;">{rec.get('inr_type','')}</td>
              <td style="padding:6px 8px;font-size:12px;">{rec.get('cr_status_name','')}</td>
              <td style="padding:6px 8px;font-size:12px;color:#C0392B;font-weight:bold;">
                ${float(rec.get('amount_at_risk', 0)):,.2f}
              </td>
              <td style="padding:6px 8px;font-size:11px;color:#666;">{rec.get('failure_reason','')[:100]}...</td>
            </tr>"""

        more_note = f"<p style='font-size:11px;color:#666;margin:4px 0;'>... and {len(records)-25} more records. See attached CSV for full list.</p>" if len(records) > 25 else ""

        sections_html += f"""
        <div style="margin:20px 0;border:1px solid #ddd;border-radius:8px;overflow:hidden;background:#fff;">
          <!-- Section Header -->
          <div style="background:{m['color']};padding:12px 16px;display:flex;align-items:center;">
            <span style="font-size:20px;margin-right:10px;">{m['icon']}</span>
            <div>
              <span style="font-size:15px;font-weight:bold;color:#fff;">{m['description']}</span>
              &nbsp;&nbsp;{badge}
              <span style="font-size:13px;color:rgba(255,255,255,0.85);margin-left:12px;">
                {data['count']} records &nbsp;|&nbsp; ${data['amount_at_risk']:,.2f} at risk
              </span>
            </div>
          </div>
          <!-- Meta Info -->
          <div style="background:{row_color};padding:10px 16px;border-bottom:1px solid #ddd;">
            <p style="margin:3px 0;font-size:12px;"><strong>Impact:</strong> {m['impact']}</p>
            <p style="margin:3px 0;font-size:12px;"><strong>Required Action:</strong>
              <span style="color:#C0392B;font-weight:bold;">{m['action']}</span></p>
            <p style="margin:3px 0;font-size:12px;color:#666;"><strong>Data Source:</strong> {m['source']}</p>
          </div>
          <!-- Detail Table -->
          <div style="overflow-x:auto;padding:0 8px 8px;">
            <table cellpadding="0" cellspacing="0" style="width:100%;border-collapse:collapse;">
              <thead>
                <tr style="background:#F2F3F4;">
                  <th style="padding:8px;text-align:left;font-size:11px;color:#555;border-bottom:2px solid #ddd;">GINR ID</th>
                  <th style="padding:8px;text-align:left;font-size:11px;color:#555;border-bottom:2px solid #ddd;">INR ID</th>
                  <th style="padding:8px;text-align:left;font-size:11px;color:#555;border-bottom:2px solid #ddd;">Company</th>
                  <th style="padding:8px;text-align:left;font-size:11px;color:#555;border-bottom:2px solid #ddd;">Type</th>
                  <th style="padding:8px;text-align:left;font-size:11px;color:#555;border-bottom:2px solid #ddd;">INR Type</th>
                  <th style="padding:8px;text-align:left;font-size:11px;color:#555;border-bottom:2px solid #ddd;">CR Status</th>
                  <th style="padding:8px;text-align:left;font-size:11px;color:#555;border-bottom:2px solid #ddd;">$ At Risk</th>
                  <th style="padding:8px;text-align:left;font-size:11px;color:#555;border-bottom:2px solid #ddd;">Issue Detail</th>
                </tr>
              </thead>
              <tbody>{detail_rows}</tbody>
            </table>
            {more_note}
          </div>
        </div>"""

    # ── No failures message ──────────────────────────────────────────────────
    if not summary:
        sections_html = """
        <div style="text-align:center;padding:40px;background:#EAFAF1;border-radius:8px;margin:20px 0;">
          <div style="font-size:48px;">✅</div>
          <h2 style="color:#27AE60;margin:10px 0;">All Payment Records Clean</h2>
          <p style="color:#666;">No payment failures detected in today's scan.</p>
        </div>"""

    # ── Full HTML template ───────────────────────────────────────────────────
    ai_summary_block = ""
    if ai_summary:
        ai_summary_html = ai_summary.replace("\n", "<br>")
        ai_summary_block = f"""
        <div style="margin:12px 0 20px;padding:14px 16px;background:#F8F9FA;border-left:4px solid #1A5276;border-radius:6px;">
          <h3 style="margin:0 0 8px;font-size:14px;color:#1A5276;">AI Executive Summary (Ollama)</h3>
          <p style="margin:0;font-size:12px;color:#2C3E50;line-height:1.5;">{ai_summary_html}</p>
        </div>"""

    html = f"""
<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0"></head>
<body style="margin:0;padding:0;font-family:Arial,sans-serif;background:#F4F6F9;">
  <div style="max-width:950px;margin:20px auto;background:#fff;border-radius:10px;
              box-shadow:0 2px 8px rgba(0,0,0,0.12);overflow:hidden;">

    <!-- ═══ HEADER ════════════════════════════════════════════════ -->
    <div style="background:#1A252F;padding:20px 30px;display:flex;align-items:center;">
      <div>
        <div style="font-size:11px;color:#7F8C8D;letter-spacing:2px;text-transform:uppercase;">
          ERCOT RIOO-IS | GINR Payment Monitor</div>
        <h1 style="margin:4px 0;font-size:22px;color:#fff;">Daily Payment Failure Report</h1>
        <div style="font-size:13px;color:#AAB7B8;">
          Generated: {datetime.datetime.now().strftime("%B %d, %Y at %I:%M %p CST")}
          &nbsp;|&nbsp; Report Date: {run_date}
        </div>
      </div>
    </div>

    <!-- ═══ ALERT BANNER ══════════════════════════════════════════ -->
    <div style="background:{banner_color};padding:14px 30px;">
      <span style="font-size:16px;font-weight:bold;color:#fff;">{banner_label}</span>
      <span style="font-size:13px;color:rgba(255,255,255,0.9);margin-left:15px;">
        {total_fail} payment issue(s) detected &nbsp;|&nbsp; ${total_risk:,.2f} total at risk
      </span>
    </div>

    <div style="padding:20px 30px;">

      <!-- ═══ SUMMARY CARDS ════════════════════════════════════════ -->
      {cards_html}
      {ai_summary_block}

      <!-- ═══ FAILURE SECTIONS ══════════════════════════════════════ -->
      <h2 style="margin:25px 0 10px;font-size:16px;color:#2C3E50;border-bottom:2px solid #E8E8E8;
                 padding-bottom:8px;">
        Failure Details by Category
      </h2>
      {sections_html}

      <!-- ═══ SQL ORACLE QUERIES ════════════════════════════════════ -->
      <div style="background:#2C3E50;border-radius:8px;padding:16px 20px;margin:20px 0;">
        <h3 style="color:#ECF0F1;margin:0 0 10px;font-size:13px;">
          🔍 Oracle Verification Queries (run in RIOO DB)
        </h3>
        <pre style="color:#2ECC71;font-size:11px;margin:0;overflow-x:auto;line-height:1.6;">
-- Unpaid FIS Fees:
SELECT gr.id, gr.inr_id, gr.fis_fee, cr.change_request_status_id
FROM ginr.ginr_request gr JOIN change_requests cr ON cr.ginr_request_id = gr.id
WHERE gr.fis_fee > 0 AND gr.fis_fee_paid = 0 AND cr.change_request_status_id IN (2,3);

-- Payment Sync Errors:
SELECT gr.id, gpd.trans_id, gpd.date_paid, gr.fis_fee_paid
FROM ginr.ginr_request gr JOIN ginr_payment_data_vw gpd ON gpd.rscr_id = cr.id
WHERE gpd.date_paid IS NOT NULL AND gr.fis_fee_paid = 0;

-- Duplicate Payments:
SELECT id_change_request, COUNT(*) cnt
FROM ginr_payment_data_vw GROUP BY id_change_request HAVING COUNT(*) > 1;
        </pre>
      </div>

    </div>

    <!-- ═══ FOOTER ════════════════════════════════════════════════ -->
    <div style="background:#F2F3F4;padding:14px 30px;border-top:1px solid #ddd;">
      <table style="width:100%;"><tr>
        <td style="font-size:11px;color:#7F8C8D;">
          🤖 {APP_INFO['name']} v{APP_INFO['version']} &nbsp;|&nbsp; System: {APP_INFO['system']}
          &nbsp;|&nbsp; <a href="{APP_INFO['dashboard']}" style="color:#3498DB;">Open Dashboard</a>
        </td>
        <td style="text-align:right;font-size:11px;color:#7F8C8D;">
          Questions? <a href="mailto:{APP_INFO['support']}" style="color:#3498DB;">{APP_INFO['support']}</a>
        </td>
      </tr></table>
    </div>
  </div>
</body>
</html>"""
    return html


# ─────────────────────────────────────────────────────────────────────────────
# CSV Attachment Builder
# ─────────────────────────────────────────────────────────────────────────────

def build_csv_attachment(report: dict) -> tuple[bytes, str]:
    """Build CSV bytes of all failures for email attachment."""
    rows = []
    for ftype, data in report["summary_by_type"].items():
        for rec in data["records"]:
            row = {
                "failure_type":    ftype,
                "severity":        data["severity"],
                "ginr_request_id": rec.get("ginr_request_id"),
                "inr_id":          rec.get("inr_id"),
                "cr_id":           rec.get("cr_id"),
                "company_name":    rec.get("company_name"),
                "company_duns":    rec.get("company_duns"),
                "resource_type":   rec.get("resource_type"),
                "inr_type":        rec.get("inr_type"),
                "cr_status":       rec.get("cr_status_name"),
                "days_in_pending": rec.get("days_in_pending"),
                "fis_fee":         rec.get("fis_fee"),
                "fis_fee_paid":    rec.get("fis_fee_paid"),
                "ss_fee":          rec.get("ss_fee"),
                "ss_fee_paid":     rec.get("ss_fee_paid"),
                "analysis_fee":    rec.get("analysis_fee"),
                "analysis_fee_paid": rec.get("analysis_fee_paid"),
                "payment_trans_id": rec.get("payment_trans_id"),
                "payment_date":    rec.get("payment_date"),
                "amount_paid":     rec.get("payment_amount_paid"),
                "amount_at_risk":  rec.get("amount_at_risk"),
                "first_name":      rec.get("first_name"),
                "last_name":       rec.get("last_name"),
                "issue_detail":    rec.get("failure_reason"),
                "detected_date":   rec.get("detected_date"),
            }
            rows.append(row)

    if not rows:
        return b"No failures detected.", "no_failures.csv"

    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)

    today = report["run_date"]
    filename = f"GINR_Payment_Failures_{today}.csv"
    return buffer.getvalue().encode("utf-8"), filename


# ─────────────────────────────────────────────────────────────────────────────
# Email Sender
# ─────────────────────────────────────────────────────────────────────────────

def send_email(report: dict, dry_run: bool = False) -> dict:
    """
    Build and send the payment failure report email.

    Args:
        report:  Output from payment_failure_analyzer.run_analysis()
        dry_run: If True, skip actual SMTP send (saves HTML preview locally)

    Returns:
        dict with status, recipients, html_preview_path
    """
    LOG.info("Building email report...")
    html_body     = build_html_email(report)
    csv_bytes, csv_filename = build_csv_attachment(report)

    # Save HTML preview for inspection
    preview_path = REPORT_DIR / f"payment_report_{report['run_date']}.html"
    preview_path.write_text(html_body, encoding="utf-8")
    LOG.info(f"HTML preview saved: {preview_path}")

    # Save CSV report
    csv_path = REPORT_DIR / csv_filename
    csv_path.write_bytes(csv_bytes)
    LOG.info(f"CSV report saved: {csv_path}")

    total_fail = report["total_failures"]
    critical   = report["critical_count"]

    # Email subject with urgency prefix
    if critical > 0:
        subject = f"🔴 CRITICAL: {critical} GINR Payment Failures — ${report['total_at_risk']:,.0f} At Risk [{report['run_date']}]"
    elif total_fail > 0:
        subject = f"⚠️ GINR Payment Report: {total_fail} Issues Detected [{report['run_date']}]"
    else:
        subject = f"✅ GINR Payment Monitor: All Clear [{report['run_date']}]"

    recipients = [EMAIL_CONFIG["manager_email"]] + EMAIL_CONFIG["cc_emails"]
    recipients = [r.strip() for r in recipients if r.strip()]

    if dry_run:
        LOG.info(f"[DRY RUN] Email NOT sent. Would have sent to: {recipients}")
        LOG.info(f"[DRY RUN] Subject: {subject}")
        LOG.info(f"[DRY RUN] Preview: {preview_path}")
        return {
            "status":           "dry_run",
            "subject":          subject,
            "recipients":       recipients,
            "html_preview":     str(preview_path),
            "csv_attachment":   str(csv_path),
            "failures_reported": total_fail,
        }

    # Build MIME message
    msg = MIMEMultipart("alternative")
    msg["Subject"]  = subject
    msg["From"]     = EMAIL_CONFIG["from_address"]
    msg["To"]       = EMAIL_CONFIG["manager_email"]
    msg["Reply-To"] = EMAIL_CONFIG["reply_to"]
    if EMAIL_CONFIG["cc_emails"]:
        msg["Cc"] = ", ".join(EMAIL_CONFIG["cc_emails"])

    msg.attach(MIMEText(html_body, "html"))

    # Attach CSV
    attachment = MIMEBase("application", "octet-stream")
    attachment.set_payload(csv_bytes)
    encoders.encode_base64(attachment)
    attachment.add_header("Content-Disposition", f'attachment; filename="{csv_filename}"')
    msg.attach(attachment)

    # Send via SMTP
    try:
        with smtplib.SMTP(EMAIL_CONFIG["smtp_host"], EMAIL_CONFIG["smtp_port"]) as server:
            server.ehlo()
            if EMAIL_CONFIG["use_tls"]:
                server.starttls()
            server.login(EMAIL_CONFIG["smtp_user"], EMAIL_CONFIG["smtp_password"])
            server.sendmail(EMAIL_CONFIG["from_address"], recipients, msg.as_string())

        LOG.info(f"✅ Email sent via {EMAIL_CONFIG['provider']} to {len(recipients)} recipient(s)")
        LOG.info(f"   Subject: {subject}")
        LOG.info(f"   To: {recipients}")
        return {
            "status":           "sent",
            "subject":          subject,
            "recipients":       recipients,
            "html_preview":     str(preview_path),
            "csv_attachment":   str(csv_path),
            "failures_reported": total_fail,
        }
    except Exception as e:
        LOG.error(f"❌ Email send failed: {e}", exc_info=True)
        return {
            "status":  "error",
            "error":   str(e),
            "subject": subject,
        }

