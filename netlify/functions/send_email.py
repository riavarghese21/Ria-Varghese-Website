# netlify/functions/send_email.py

import json
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def handler(event, context):
    data = json.loads(event["body"])
    message = Mail(
        from_email='riavarghese021@gmail.com',
        to_emails='riavarghese021@gmail.com',
        subject='New Contact Form Message',
        html_content=f"<strong>Name:</strong> {data['name']}<br><strong>Email:</strong> {data['email']}<br><strong>Message:</strong> {data['message']}"
    )

    try:
        sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
        response = sg.send(message)
        return {
            "statusCode": 200,
            "body": json.dumps({"status": "success"})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"status": "error", "message": str(e)})
        }
