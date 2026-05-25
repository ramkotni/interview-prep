from fastapi import FastAPI
from pydantic import BaseModel
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = FastAPI()

# -----------------------------
# Request Object
# -----------------------------
class PaymentRequest(BaseModel):

    credit_score: int
    prior_defaults: int
    missing_documents: int
    duplicate_submission: int
    market_price: float
    application_completion_pct: int
    bank_balance_million: float
    transaction_retry_count: int


# -----------------------------
# Email Alert Function
# -----------------------------
def send_finance_alert(risk_probability):

    sender_email = "ramkotni@gmail.com"

    app_password = "edaobpgqkjjdhovd"

    #receiver_email = "finance@ercot.com"

    receiver_email = "ramkotni@gmail.com"

    subject = "ERCOT Generator Payment Risk Alert"

    body = f"""
    High Risk Payment Detected

    Risk Probability: {risk_probability}

    Reasons:
    - Prior defaults detected
    - Missing documents
    - Financial risk identified

    Recommended Action:
    - Manual Review Required
    """

    message = MIMEMultipart()

    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:

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

        print("Finance alert email sent")

    except Exception as e:

        print("Email failed:", e)


# -----------------------------
# Prediction API
# -----------------------------
@app.post("/predict")
def predict(request: PaymentRequest):

    # -----------------------------
    # Fake Prediction Logic
    # Replace later with ML model
    # -----------------------------

    risk_probability = 0.92

    prediction = "HIGH_RISK"

    # -----------------------------
    # Trigger Finance Alert
    # -----------------------------
    if risk_probability > 0.80:

        send_finance_alert(
            risk_probability
        )

    return {
        "risk_probability": risk_probability,
        "prediction": prediction
    }