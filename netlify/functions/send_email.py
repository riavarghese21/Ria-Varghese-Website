import os
import json
import requests

def handler(event, context):
    try:
        # Parse form data from request body
        data = json.loads(event['body'])
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        # Email details
        subject = f"New Contact Form Submission from {name}"
        content = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        # Send via SendGrid API
        sendgrid_api_key = os.environ.get("SENDGRID_API_KEY")
        response = requests.post(
            "https://api.sendgrid.com/v3/mail/send",
            headers={
                "Authorization": f"Bearer {sendgrid_api_key}",
                "Content-Type": "application/json"
            },
            json={
                "personalizations": [{
                    "to": [{"email": "riavarghese021@gmail.com"}]
                }],
                "from": {"email": "no-reply@yourdomain.com"},
                "subject": subject,
                "content": [{
                    "type": "text/plain",
                    "value": content
                }]
            }
        )

        if response.status_code == 202:
            return {
                "statusCode": 200,
                "body": json.dumps({"status": "success"})
            }
        else:
            return {
                "statusCode": 500,
                "body": json.dumps({"status": "error", "message": response.text})
            }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"status": "error", "message": str(e)})
        }
