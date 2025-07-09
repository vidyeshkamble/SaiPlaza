from email.message import EmailMessage
import smtplib
import mysql
from twilio.rest import Client

import config

class FetchOTP:
    def __init__(self):
        pass

    @staticmethod
    def Connection():
        return mysql.connector.connect(
            host= config.DB_HOST, 
            user= config.DB_USER,
            password= config.DB_PASSWORD, 
            database=config.DB_NAME 
        )

    def sendEmailMessage(subject,body,to):
        msg = EmailMessage()
        msg.set_content(body)
        msg['subject'] = subject
        msg['to'] = to
        msg['form'] = 'vidyeshmy@gmail.com'
        
        user = "vidyeshmy@gmail.com"
        password = 'sqzp gcof aida usit'
        
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(user,password)
        server.send_message(msg)
        
        server.quit()
        return 
    
    def sendTextMessage(phoneNo,OTP):
        account_sid = config.TWILIO_ACCOUNT_SID
        auth_token = config.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"This is a text message from Sai Plaza. One Time Password (OTP) for your transaction is {OTP}. Please do not share this OTP with anyone.",
            from_= config.TWILIO_PHONE_NUMBER, 
            to='+91' + str(phoneNo)
        )
        return