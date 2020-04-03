import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

# https://elkton.church Email Addresses
ADMIN_ELKTON_CHURCH_EMAIL = os.environ.get('ADMIN_ELKTON_CHURCH_EMAIL')
SUPPORT_ELKTON_CHURCH_EMAIL = os.environ.get('SUPPORT_ELKTON_CHURCH_EMAIL')

# elktondotchurch@gmail.com credentials
ELKTON_DOT_CHURCH_GMAIL_USERNAME = os.environ.get('ELKTON_DOT_CHURCH_GMAIL_USERNAME')
ELKTON_DOT_CHURCH_GMAIL_PASSWORD = os.environ.get('ELKTON_DOT_CHURCH_GMAIL_PASSWORD')

# Pastoral Team's Email Addresses
PASTOR_REGGIE_EMAIL = os.environ.get('PASTOR_REGGIE_EMAIL')
SUE_COURLISS_EMAIL = os.environ.get('SUE_COURLISS_EMAIL')

# Deacons' Email Addresses
TICO_GMAIL_EMAIL = os.environ.get('TICO_GMAIL_EMAIL')
DON_FAUPEL_EMAIL = os.environ.get('DON_FAUPEL_EMAIL')
CASEY_TURNER_EMAIL = os.environ.get('CASEY_TURNER_EMAIL')
MIKE_VIERS_EMAIL = os.environ.get('MIKE_VIERS_EMAIL')

# Deaconesses' Email Addresses
MELISSA_HELMUTH_EMAIL = os.environ.get('MELISSA_HELMUTH_EMAIL')
KIM_KARL_EMAIL = os.environ.get('KIM_KARL_EMAIL')
KELLEE_ROTH_EMAIL = os.environ.get('KELLEE_ROTH_EMAIL')
PATTY_EVANS_EMAIL = os.environ.get('PATTY_EVANS_EMAIL')
JEN_VIERS_EMAIL = os.environ.get('JEN_VIERS_EMAIL')

# Sends out multiple email notifications of a new EMC prayer request
def send_mail(userFirstName, userLastName, typeOfRequest, prayerRequest):
    port = 587
    smtp_server = 'smtp.gmail.com'
    login = ELKTON_DOT_CHURCH_GMAIL_USERNAME
    password = ELKTON_DOT_CHURCH_GMAIL_PASSWORD
    message = f"<div><ul><li>Name: {userFirstName} {userLastName}</li></ul></div><div><ul><li>Type of Prayer Request: {typeOfRequest}</li></ul></div><div><ul><li>Details of Prayer Request: {prayerRequest}</li></ul></div>"
    
    # Email account that notifications will be sent from
    sender = ADMIN_ELKTON_CHURCH_EMAIL
    
    ENV = 'dev'
    
    if ENV == 'prod':
        # Church staff that will receive prayer request notifications
        recipients = [
            PASTOR_REGGIE_EMAIL, 
            SUE_COURLISS_EMAIL, 
            TICO_GMAIL_EMAIL, 
            DON_FAUPEL_EMAIL,
            CASEY_TURNER_EMAIL, 
            MIKE_VIERS_EMAIL,
            MELISSA_HELMUTH_EMAIL,
            KIM_KARL_EMAIL,
            KELLEE_ROTH_EMAIL,
            PATTY_EVANS_EMAIL,
            JEN_VIERS_EMAIL
        ]
    else:
        # Church staff that will receive prayer request notifications
        recipients = [
            TICO_GMAIL_EMAIL,
            SUPPORT_ELKTON_CHURCH_EMAIL
        ]
    

    
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