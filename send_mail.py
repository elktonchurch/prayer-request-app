import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

ELKTON_DOT_CHURCH_GMAIL_USERNAME = os.environ.get('ELKTON_DOT_CHURCH_GMAIL_USERNAME')
ELKTON_DOT_CHURCH_GMAIL_PASSWORD = os.environ.get('ELKTON_DOT_CHURCH_GMAIL_PASSWORD')
TICO_GMAIL_EMAIL = os.environ.get('TICO_GMAIL_EMAIL')

def send_mail(user, typeOfRequest, prayerRequest):
    port = 587
    smtp_server = 'smtp.gmail.com'
    login = ELKTON_DOT_CHURCH_GMAIL_USERNAME
    password = ELKTON_DOT_CHURCH_GMAIL_PASSWORD
    message = f"<ul><li>User: {user}</li><li>Type of Prayer Request: {typeOfRequest}</li><li>Prayer Request: {prayerRequest}</li></ul>"
    
    sender = ELKTON_DOT_CHURCH_GMAIL_USERNAME
    recipients = TICO_GMAIL_EMAIL
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'New EMC Prayer Request'
    msg['From'] = sender
    msg['To'] = recipients
    
    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        
        server.login(login, password)
        server.sendmail(sender, recipients, msg.as_string())