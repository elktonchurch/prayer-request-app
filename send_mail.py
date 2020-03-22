import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

ADMIN_ELKTON_CHURCH_EMAIL_ADDRESS = os.environ.get('ADMIN_ELKTON_CHURCH_EMAIL_ADDRESS')
ELKTON_DOT_CHURCH_GMAIL_USERNAME = os.environ.get('ELKTON_DOT_CHURCH_GMAIL_USERNAME')
ELKTON_DOT_CHURCH_GMAIL_PASSWORD = os.environ.get('ELKTON_DOT_CHURCH_GMAIL_PASSWORD')

# Pastor's Email
PASTOR_REGGIE_EMAIL = os.environ.get('PASTOR_REGGIE_EMAIL')

# Deacons' Emails
TICO_GMAIL_EMAIL = os.environ.get('TICO_GMAIL_EMAIL')
TICO2_GMAIL_EMAIL = os.environ.get('TICO2_GMAIL_EMAIL')
DON_FAUPEL_EMAIL = os.environ.get('DON_FAUPEL_EMAIL')
CASEY_TURNER_EMAIL = os.environ.get('CASEY_TURNER_EMAIL')
MIKE_VIERS_EMAIL = os.environ.get('MIKE_VIERS_EMAIL')

# Deaconesses' Emails




def send_mail(user, typeOfRequest, prayerRequest):
    port = 587
    smtp_server = 'smtp.gmail.com'
    login = ELKTON_DOT_CHURCH_GMAIL_USERNAME
    password = ELKTON_DOT_CHURCH_GMAIL_PASSWORD
    message = f"<div><ul><li>Name: {user}</li></ul></div><div><ul><li>Type of Prayer Request: {typeOfRequest}</li></ul></div><div><ul><li>Details of Prayer Request: {prayerRequest}</li></ul></div>"
    
    sender = ADMIN_ELKTON_CHURCH_EMAIL_ADDRESS
    recipients = [PASTOR_REGGIE_EMAIL, TICO2_GMAIL_EMAIL, DON_FAUPEL_EMAIL, CASEY_TURNER_EMAIL, MIKE_VIERS_EMAIL]
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'New EMC Prayer Request'
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    
    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        
        server.login(login, password)
        server.sendmail(sender, recipients, msg.as_string())