import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import email, smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import config 


def checkLog():
    if os.stat("/Users/maxhager/Projects2022/CronjobManager/cronjob.txt").st_size != 0:
        mail("/Users/maxhager/Projects2022/CronjobManager/cronjob.txt")
    elif os.stat("/Users/maxhager/Projects2022/CronjobManager/cronjobGit.txt").st_size != 0:
        findPattern()
    else:
        pass
        

def mail(file):
    sender_email = "maxhager28@gmail.com"
    receiver_email = "maxhager28@gmail.com"
    password = config.password
    body = "A message from a cronjob."
    message = MIMEMultipart("alternative")
    message["Subject"] = "Cronjob"
    message["From"] = sender_email
    message["To"] = receiver_email
    message.attach(MIMEText(body, "plain"))
    filename = file
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    message.attach(part)
    text = message.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
    
        
    
    
def findPattern():
    with open("/Users/maxhager/Projects2022/CronjobManager/cronjobGit.txt", "r") as f:
        firstLine = f.readline()
    print(firstLine[0:14])
    print(firstLine[0:5])
    if firstLine[0:14] != "On branch main" and firstLine[0:5] != "[main":
        mail("/Users/maxhager/Projects2022/CronjobManager/cronjobGit.txt")


if __name__ == "__main__":
    checkLog()