from app import mail
from flask_mail import Message
from flask import current_app


def send_email(body):
    msg = Message(subject="Application Submission",
                  recipients=[current_app.config['MAIL_USERNAME']],
                  body=body)
    msg.sender = current_app.config['MAIL_DEFAULT_SENDER']
    return mail.send(msg)