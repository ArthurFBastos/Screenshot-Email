import os
from dotenv import load_dotenv

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail,Attachment,FileContent,FileName,FileType,Disposition)

import pybase64

load_dotenv()

def send_email(path,date):
    message = Mail(
    from_email=os.getenv("login"),
    to_emails=os.getenv("send_to"),
    subject='Sending with Twilio SendGrid is Fun',
    html_content="""
        <b> Title </b>
        <p> First text line </p>
        """
    )

    with open(path, 'rb') as f:
        data = f.read()
        f.close()
    encoded_file = pybase64.b64encode(data).decode()

    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName(f'Print  {date}.png'),
        FileType('Print/png'),
        Disposition('attachment')
    )
    message.attachment = attachedFile

    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code, response.body, response.headers)