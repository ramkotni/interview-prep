import pandas as pd
import ollama
import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ==================================================
# STEP 1 - LOAD PREDICTION CSV
# ==================================================

print("Loading prediction dataset...")

df = pd.read_csv(
    "data/output/payment_risk_predictions.csv"
)

# ==================================================
# STEP 2 - CALCULATE BUSINESS METRICS
# ==================================================

total_transactions = len(df)

# Predicted failed transactions
predicted_failures = len(
    df[df["PREDICTED_STATUS"] == 1]
)

# High-risk transactions
high_risk = len(
    df[df["FAILURE_PROBABILITY"] >= 0.80]
)

# Medium-risk transactions
medium_risk = len(
    df[
        (df["FAILURE_PROBABILITY"] >= 0.30)
        &
        (df["FAILURE_PROBABILITY"] < 0.80)
    ]
)

# Average risk score
average_risk = round(
    df["FAILURE_PROBABILITY"].mean(),
    2
)

# Top risky application size
top_application_size = (
    df["RISK_LEVEL"]
    .value_counts()
    .idxmax()
)

# ==================================================
# STEP 3 - BUILD AI PROMPT
# ==================================================

prompt = f"""
You are an ERCOT finance AI reporting assistant.

Generate ONLY a professional
monthly finance summary email.

DO NOT:
- give multiple options
- ask questions
- add markdown
- add explanations
- add conversational text

Write only the final email.

Monthly Risk Statistics:

Total Transactions:
{total_transactions}

Predicted Failed Transactions:
{predicted_failures}

High Risk Transactions:
{high_risk}

Medium Risk Transactions:
{medium_risk}

Average Failure Probability:
{average_risk}

Top Risk Category:
{top_application_size}

Include:
1. Executive Summary
2. Payment Failure Analysis
3. Business Risk Impact
4. Operational Concerns
5. Recommendations
6. Next Month Action Plan

Keep it concise,
executive-level,
and professional.
"""

# ==================================================
# STEP 4 - GENERATE AI REPORT
# ==================================================

print("Generating AI summary...")

response = ollama.chat(
    model="gemma3:1b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

ai_summary = response["message"]["content"]

print("\n===== AI GENERATED REPORT =====\n")
print(ai_summary)

# ==================================================
# STEP 5 - SAVE REPORT TO FILE
# ==================================================

os.makedirs("reports", exist_ok=True)

report_file = (
    "reports/monthly_payment_report.txt"
)

with open(report_file, "w") as file:
    file.write(ai_summary)

print(f"\nReport saved: {report_file}")

# ==================================================
# STEP 6 - SEND EMAIL
# ==================================================

sender_email = "ramkotni@gmail.com"

app_password = "edaobpgqkjjdhovd"

receiver_email = "ramkotni@gmail.com"

message = MIMEMultipart()

message["From"] = sender_email
message["To"] = receiver_email

message["Subject"] = (
    "Monthly ERCOT Payment Risk Report"
)

message.attach(
    MIMEText(ai_summary, "plain")
)

print("\nSending email...")

server = smtplib.SMTP(
    "smtp.gmail.com",
    587
)

server.starttls()

server.login(
    sender_email,
    app_password
)

server.sendmail(
    sender_email,
    receiver_email,
    message.as_string()
)

server.quit()

print("\nMonthly report email sent successfully.")