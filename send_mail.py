import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

# elkton.church email addresses
ADMIN_ELKTON_CHURCH_EMAIL = os.environ.get('ADMIN_ELKTON_CHURCH_EMAIL')
SUPPORT_ELKTON_CHURCH_EMAIL = os.environ.get('SUPPORT_ELKTON_CHURCH_EMAIL')

# elktondotchurch gmail addresses
ELKTON_DOT_CHURCH_GMAIL_USERNAME = os.environ.get('ELKTON_DOT_CHURCH_GMAIL_USERNAME')
ELKTON_DOT_CHURCH_GMAIL_PASSWORD = os.environ.get('ELKTON_DOT_CHURCH_GMAIL_PASSWORD')

# Deacons' Email Addresses
TICO_GMAIL_EMAIL = os.environ.get('TICO_GMAIL_EMAIL')

# Sends out multiple email notifications of a new EMC prayer request
def send_mail(userFirstName, userLastName, typeOfRequest, prayerRequest):
    port = 587
    smtp_server = 'smtp.gmail.com'
    login = ELKTON_DOT_CHURCH_GMAIL_USERNAME
    password = ELKTON_DOT_CHURCH_GMAIL_PASSWORD
    message = f"<div><ul><li>Name: {userFirstName} {userLastName}</li></ul></div><div><ul><li>Type of Prayer Request: {typeOfRequest}</li></ul></div><div><ul><li>Details of Prayer Request: {prayerRequest}</li></ul></div>"
    
    # Email account that notifications will be sent from
    sender = ADMIN_ELKTON_CHURCH_EMAIL
    
    # Church staff that will receive prayer request notifications
    recipients = [TICO_GMAIL_EMAIL, SUPPORT_ELKTON_CHURCH_EMAIL]
    
    
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'New EMC Prayer Request'
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    
    # Sends email to recipients via TLS (transport layer security)
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()
        
        server.login(login, password)
        server.sendmail(sender, recipients, msg.as_string())