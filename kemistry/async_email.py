from flask_security import MailUtil
from flask_mailman import EmailMessage
from threading import Thread
from flask import current_app


class MyMailUtil(MailUtil):
    """
    Custom MailUtil class for sending emails asynchronously using threads.
    """

    def send_mail(self, template, subject, recipient, sender, body, html, **kwargs):
        """
        Send an email asynchronously using threads.

        Args:
            template: Email template.
            subject: Email subject.
            recipient: Email recipient.
            sender: Email sender.
            body: Email body.
            html: HTML content of the email.
            **kwargs: Additional keyword arguments.

        Returns:
            Thread: The thread object responsible for sending the email asynchronously.
        """
        msg = EmailMessage(
            subject=subject, from_email=sender, to=[recipient], body=body
        )

        thread = Thread(
            target=send_async_email, args=(current_app._get_current_object(), msg)
        )
        thread.start()

        return thread


def send_async_email(app, msg):
    """
    Function to send an email asynchronously in a separate thread.

    Args:
        app: The Flask application object.
        msg (EmailMessage): The EmailMessage object containing email details.

    Returns:
        None
    """
    from kemistry import mail

    with app.app_context():
        with mail.get_connection() as connection:
            email_message = EmailMessage(
                subject=msg.subject,
                body=msg.body,
                from_email=msg.from_email,
                to=msg.to,
                connection=connection,
            )

            email_message.send()
