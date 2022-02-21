import os
from dotenv import load_dotenv

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail,Attachment,FileContent,FileName,FileType,Disposition)

import pybase64

load_dotenv()

def send_email(path,date):
    #Create the email body with .env data
    message = Mail(
    from_email=os.getenv("login"),
    to_emails=os.getenv("send_to"),
    subject='Write a subject',
    html_content="""
        <b> Title </b>
        <p> First text line </p>
        """
    )
    #Open the archive path an read the data in base64
    with open(path, 'rb') as f:
        data = f.read()
        f.close()
    encoded_file = pybase64.b64encode(data).decode()
    #Select the encoded file and write the name and type that will show on the email
    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName(f'Print  {date}.png'),
        FileType('Print/png'),
        Disposition('attachment')
    )
    #Attach the file 
    message.attachment = attachedFile

    #Enter SendGrid API with the user key (must be changed in the .env)
    sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
    
    #Consume the SendGrid API and send the email
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)