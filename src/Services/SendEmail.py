import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders
from Services.PrintWeb import print_web

import os
from dotenv import load_dotenv

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()


def send_email2():
    message = Mail(
        from_email=os.getenv("login"),
        to_emails=os.getenv("send_to"),
        subject='Sending with Twilio SendGrid is Fun',
        html_content="""
        <b> Title </b>
        <p> First text line </p>
        """
    )

    sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)



def send_email(path):

    #Set SMTP server and login in your email
    host = os.getenv("host")
    port = os.getenv("port")
    login = os.getenv("login")
    password = os.getenv("senha")
    send_to = os.getenv("send_to")

    #Starting the server
    server = smtplib.SMTP(host,port)
    server.ehlo()
    server.starttls()
    server.login(login,password)


    #Write MIME type email in html
    body = """
    <b> Title </b>
    <p> First text line </p>
    """


    #Build email body
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = send_to
    email_msg['Subject'] = "Write a subject"
    email_msg.attach(MIMEText(body,'html'))

    #Open the archive in reading mode, must be binary
    path_arquive = f"{path}"
    attchment = open(path_arquive,'rb')

    #We read the file in binary mode and play it encoded in base 64 (which is what email needs)
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)

    #Added header in email attachment type
    att.add_header('Content-Disposition', f'attachment; filename=Archive_name.jpg')
    
    #Close the archive
    attchment.close()

    #Add the attachment to the body
    email_msg.attach(att)

    #Send MIME type email on SMTP server
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())
    server.quit()