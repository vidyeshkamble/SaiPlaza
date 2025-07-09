import datetime
import imaplib
from email import message_from_bytes
import re
import socket
import threading
import time
import config


class PaymentGetway:
    
    def __init__(self):
        pass
    
    def clientCall(self,amount,upiId):
        try: 
            server_thread = threading.Thread(target=self.start_socket_server,args=(amount, upiId), daemon = True)
            server_thread.start()
            time.sleep(1)
            s = socket.socket()
            
            
            print("wating For connection to Server......!")
            time.sleep(1)
            s.connect(('localhost',12345))
            print("Client: Connected!")
            msg = s.recv(1024).decode()
            
            if msg.lower() == 'no':
                print("Client Pending....!")
                return False
            
            return msg
            
        except Exception as e:
            print(e)
        finally:        
            s.close() 
        
    def start_socket_server(self,amount,upiId):
        import socket
        server_socket = socket.socket()
        server_socket.bind(('localhost',12345))
        server_socket.listen(1)
        print("Server: Waiting for client connection...")
        conn, addr = server_socket.accept()
        
        send_date = str(datetime.datetime.now().strftime("%d-%m-%y"))   
        time.sleep(25)
        
        varification = self.readEmail(amount,upiId,send_date)
        if varification:
            conn.send(varification.encode())
        else:
            conn.send("no".encode())    
                
                   
    
    def readEmail(self, AMOUNT, UPI_ID, SEND_DATE):
        try:
            BANK_EMAIL_ID = config.BANK_EMAIL_ID
            BANK_EMAIL_SUBJECT = 'View: Account update for your HDFC Bank A/c'
            STATEMENT_DONE = 'successfully credited'
            
            MAIL_USERNAME = config.MAIL_USERNAME
            MAIL_PASSWORD = config.MAIL_PASSWORD
            
            mail = imaplib.IMAP4_SSL("imap.gmail.com")
            mail.login(MAIL_USERNAME, MAIL_PASSWORD)

            timeout = time.time() + 60 
            while time.time() < timeout:
                print("Checking Email wait.......!")
                mail.select("inbox")  
                status, folders = mail.search(None, f'(FROM "{BANK_EMAIL_ID}" SUBJECT "{BANK_EMAIL_SUBJECT}")')
                email_ids = folders[0].split()

                for email_id in reversed(email_ids):  # Check newest emails first
                    status, folders = mail.fetch(email_id, '(RFC822)')
                    msg = message_from_bytes(folders[0][1])

                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True).decode()

                            if all(k in body for k in [AMOUNT, UPI_ID, SEND_DATE, STATEMENT_DONE]):
                                print("Subject :", msg.get('Subject'))
                                print("From : ", msg.get('From'))

                                # ✅ Delete the email
                                mail.store(email_id, '+FLAGS', '\\Deleted')
                                mail.expunge()  # permanently deletes marked emails

                                # ✅ Return UPI reference
                                match = re.search(r"Your UPI transaction reference number is (\d+)", body)
                                if match:
                                    return match.group(1)

                time.sleep(5)  

            print("Not Found....!")
            return False

        except Exception as e:
            print(e)
            return False

        finally:
            mail.close()
            mail.logout()