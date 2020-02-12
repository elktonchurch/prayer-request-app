import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

MAILTRAP_USERNAME = os.environ.get('MAILTRAP_USERNAME')
MAILTRAP_PASSWORD = os.environ.get('MAILTRAP_PASSWORD')
TICO_GMAIL_EMAIL = os.environ.get('TICO_GMAIL_EMAIL')
ELKTONMC_LIVE_EMAIL = os.environ.get('ELKTONMC_LIVE_EMAIL')

def send_mail(user, typeOfRequest, prayerRequest):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = MAILTRAP_USERNAME
    password = MAILTRAP_PASSWORD
    message = f"<h3>New Prayer Request Submission</h3><ul><li>User: {user}</li><li>Type of Prayer Request: {typeOfRequest}</li><li>Prayer Request: {prayerRequest}</li></ul>"
    
    sender_email = ELKTONMC_LIVE_EMAIL
    receiver_email = TICO_GMAIL_EMAIL
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'EMC Prayer Request'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())