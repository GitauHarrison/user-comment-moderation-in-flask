from flask_mail import Message
from app import mail, app
from flask import render_template
from threading import Thread


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()


def send_live_comment_email(user):
    send_mail(
        '[Your Comment Is Live]',
        sender=app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('email/live_comment.txt', user=user),
        html_body=render_template('email/live_comment.html', user=user)
    )
