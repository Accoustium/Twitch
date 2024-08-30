import os
import dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(subject: str, html_content: str):
    if dotenv.load_dotenv("./smtp/.env"):
        message = Mail(
            from_email=os.environ.get('EMAIL_SENDER'),
            to_emails=os.environ.get('EMAIL_RECEIVER'),
            subject=subject,
            html_content=html_content
        )

        try:
            sg = SendGridAPIClient(os.environ.get('SMTP_PASS'))
            response = sg.send(message)
            if response.status_code == 200:
                print("Email Successfully Sent")
            else:
                print("Email Failed to Send")
        except Exception as e:
            print(e.args)
    else:
        print("Unable to load environment variables")
