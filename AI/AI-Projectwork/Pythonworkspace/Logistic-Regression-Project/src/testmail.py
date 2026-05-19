import smtplib

sender_email = "ramkotni@gmail.com"
app_password = "ozdhekubjadtuzks"

receiver_email = "ramkotni@gmail.com"

try:

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.ehlo()

    server.starttls()

    server.ehlo()

    server.login(sender_email, app_password)

    print("Login successful")

    message = """
Subject: Test Mail

Hello,
This is a test email from Python.
"""

    server.sendmail(
        sender_email,
        receiver_email,
        message
    )

    print("Email sent successfully")

    server.quit()

except Exception as e:
    print(e)