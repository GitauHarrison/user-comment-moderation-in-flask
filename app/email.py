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


# ---------------------
# Password Reset Email
# ---------------------


def send_password_reset_email(admin):
    token = admin.get_reset_password_token()
    send_mail(
        '[Password Reset]',
        sender=app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('email/reset_password.txt',
                                  admin=admin,
                                  token=token),
        html_body=render_template('email/reset_password.html',
                                  admin=admin,
                                  token=token)
    )


# -----------------------------------
# Comment Is Live Email Notification
# -----------------------------------


def article1_send_live_comment_email(user):
    send_mail(
        '[Your Comment Is Live: Article 1]',
        sender=app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('email/article1_live_comment.txt',
                                  user=user),
        html_body=render_template('email/article1_live_comment.html',
                                  user=user)
    )


def article2_send_live_comment_email(user):
    send_mail(
        '[Your Comment Is Live: Article 2]',
        sender=app.config['ADMINS'][0],
        recipients=[user.email],
        text_body=render_template('email/article2_live_comment.txt',
                                  user=user),
        html_body=render_template('email/article2_live_comment.html',
                                  user=user)
    )

# ------------------------------------
# New Comment Email Notification
# ------------------------------------


def article1_send_comment_notification(admin):
    send_mail(
        '[New Comment: Article 1]',
        sender=app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('email/article1_new_comment.txt',
                                  admin=admin),
        html_body=render_template('email/article1_new_comment.html',
                                  admin=admin)
    )


def article2_send_comment_notification(admin):
    send_mail(
        '[New Comment: Article 2]',
        sender=app.config['ADMINS'][0],
        recipients=[admin.email],
        text_body=render_template('email/article2_new_comment.txt',
                                  admin=admin),
        html_body=render_template('email/article2_new_comment.html',
                                  admin=admin)
    )
