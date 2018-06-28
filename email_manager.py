"""The first step is to create an SMTP object, each object is used for connection 
with one server."""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CREDENTIALS = "credentials.txt" # file format: first line user name, second line password

def connect():
    try:  
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        return server
    except:  
        print('Something went wrong...')
        return None


def login(server):
    f = open(CREDENTIALS, "r")
    lines = list(f.readlines())
    server.login( lines[0], lines[1])
    return lines[0]


def send(sender, recipients, subject,body , server):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server.sendmail( sender, recipients, msg.as_string())


server = connect()
username = login(server)
send( username, [username], "whatup", "works", server)
