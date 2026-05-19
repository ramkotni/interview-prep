import json
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# -----------------------------
# OLLAMA SETTINGS
# -----------------------------
OLLAMA_URL = "http://localhost:11434/api/generate"

# -----------------------------
# EMAIL SETTINGS
# -----------------------------
sender_email = "ramkotni@gmail.com"
app_password = "edaobpgqkjjdhovd"   # replace with NEW app password if needed
receiver_email = "ramkotni@gmail.com"

print("DEBUG EMAIL:", sender_email)
print("DEBUG PASS LENGTH:", len(app_password))
print("DEBUG PASS VALUE:", repr(app_password))

# -----------------------------
# INPUT JSON
# -----------------------------
data = {
    "asset": "solar panel",
    "recipient": "Kalyan",
    "date": "05-20-2026",
    "subject": "Generator Failure",
    "action": "Check your connectivity or any issues"
}

# -----------------------------
# PROMPT (STRICT OUTPUT CONTROL)
# -----------------------------
prompt = f"""
You are an email generator.

Return ONLY a professional email body.

Rules:
- No JSON
- No explanations
- No options
- No markdown
- No subject line

Use this data:
{json.dumps(data, indent=2)}
"""

# -----------------------------
# OLLAMA REQUEST
# -----------------------------
payload = {
    "model": "gemma3:1b",
    "prompt": prompt,
    "stream": False
}

try:
    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    result = response.json()
    email_body = result["response"].strip()

    print("\nGenerated Email:\n")
    print(email_body)

    # -----------------------------
    # CREATE EMAIL
    # -----------------------------
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = data["subject"]

    message.attach(MIMEText(email_body, "plain"))

    # -----------------------------
    # SMTP CONNECTION (GMAIL)
    # -----------------------------
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # LOGIN
    server.login(sender_email.strip(), app_password.strip())

    # SEND EMAIL (IMPORTANT FIX: use sendmail)
    server.sendmail(
        sender_email,
        receiver_email,
        message.as_string()
    )

    server.quit()

    print("\nEmail sent successfully!")

except requests.exceptions.RequestException as e:
    print("\nOllama API Error:", e)

except smtplib.SMTPAuthenticationError:
    print("\nGmail Authentication Failed - check app password")

except Exception as e:
    print("\nERROR:", e)