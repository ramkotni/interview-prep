import smtplib

from email.mime.text import MIMEText

def send_email(state):

    report = state["executive_report"]

    sender = "ramkotni@gmail.com"

    password = "edaobpgqkjjdhovd"

    receiver = "ramkotni@gmail.com"

    msg = MIMEText(report)

    msg["Subject"] = (
        "ERCOT Monthly AI Risk Report"
    )

    msg["From"] = sender

    msg["To"] = receiver

    server = smtplib.SMTP(
        "smtp.gmail.com",
        587
    )

    server.starttls()

    server.login(sender, password)

    server.sendmail(
        sender,
        receiver,
        msg.as_string()
    )

    server.quit()

    print("Email sent")

    return state