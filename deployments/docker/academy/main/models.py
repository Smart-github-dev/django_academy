from django.conf import settings
from email.message import EmailMessage
import smtplib
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxLengthValidator
from jsonfield import JSONField
from datetime import datetime, timedelta
from django.utils import timezone


class Feature(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    feature_type = models.CharField(max_length=60, default="Basic")
    payment_confirmation = models.BooleanField(default=False)
    created_at = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="last update", auto_now_add=True)

    def __str__(self):
        return self.user.username


class SecureShell(models.Model):
    created_at = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="last update", auto_now_add=True)
    owner = models.CharField(max_length=60, null=True)
    private_key = models.CharField(max_length=16384, null=True)

    def __str__(self):
        return self.owner


class Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    first_name = models.CharField(max_length=60, null=True)
    last_name = models.CharField(max_length=60, null=True)
    email = models.EmailField(max_length=120, null=True)
    subject = models.CharField(max_length=120, null=True)
    body = models.CharField(max_length=750, null=True)
    answer = models.TextField(
        max_length=750, blank=True, validators=[MaxLengthValidator(750)]
    )
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.subject


class JsonStore(models.Model):
    name = models.CharField(max_length=100, null=True)
    data = JSONField(null=True)
    created_date = models.DateTimeField(
        blank=True, null=True, help_text="HH:MM:SS DD Mmm YY, YYYY CDT"
    )
    updated_date = models.DateTimeField(
        blank=True, null=True, help_text="HH:MM:SS DD Mmm YY, YYYY CDT"
    )


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f" you have a question from : " + f"{self.user}"


def save_notification(sender, instance, **kwargs):
    notification = Notification.objects.create(user=instance.user)


post_save.connect(save_notification, sender=Questions)


# generating the e-mail template
class NewsletterEmailer:
    email = getattr(settings, "EMAIL_HOST_USER", None)
    password = getattr(settings, "EMAIL_HOST_PASSWORD", None)

    msg = EmailMessage()

    def send_email(self, email, txt_template=None):
        self.msg["Subject"] = "Welcome to FuChiCorp!"
        self.msg["From"] = "settings.EMAIL_HOST_USER"
        self.msg["To"] = email

        if txt_template is None:
            self.msg.add_alternative(
                """\
                <html>
                    <head>
                    </head>
                    <body">
                    <center>
                        <h1 style="color: linear-gradient(to top, #a18cd1 0%, #fbc2eb 100%); font-weight: bold;"> Welcome To FuChiCorp-Pynote </h1>
                        <h5>Thank you for joing our newsletter </h5>
                        <h4>Check our website for more detials : <a style="color:blue;">https://academy.fuchicorp.com</a></h4>
                    </center>
                    </body>
                </html>
            """,
                subtype="html",
            )

        else:
            self.msg.add_alternative(txt_template, subtype="html")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(self.email, self.password)
            smtp.send_message(self.msg)


class FAQEmailer:
    email = getattr(settings, "EMAIL_HOST_USER", None)
    password = getattr(settings, "EMAIL_HOST_PASSWORD", None)

    msg = EmailMessage()

    def send_email(self, email, txt_template=None):
        self.msg["Subject"] = "Thank you for contacting us!"
        self.msg["From"] = "settings.EMAIL_HOST_USER"
        self.msg["To"] = email

        if txt_template is None:
            self.msg.add_alternative(
                """\
                <html>
                    <head>
                    </head>
                    <body">
                    <center>
                        <h1 style="color: linear-gradient(to top, #a18cd1 0%, #fbc2eb 100%); font-weight: bold;"> Your question was submitted! </h1>
                        <h5>you will receive an answer as soon as possible by one of our admins </h5>
                        <h4>Check our website for more detials : <a style="color:blue;">https://academy.fuchicorp.com</a></h4>
                    </center>
                    </body>
                </html>
            """,
                subtype="html",
            )

        else:
            self.msg.add_alternative(txt_template, subtype="html")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(self.email, self.password)
            smtp.send_message(self.msg)


class AdminEmailer:
    email = getattr(settings, "EMAIL_HOST_USER", None)
    password = getattr(settings, "EMAIL_HOST_PASSWORD", None)

    msg = EmailMessage()

    def send_email(self, email, txt_template=None):
        self.msg["Subject"] = "Dedicated message for admins!"
        self.msg["From"] = "settings.EMAIL_HOST_USER"
        self.msg["To"] = email

        if txt_template is None:
            self.msg.add_alternative(
                """\
                <html>
                    <head>
                    </head>
                    <body">
                    <center>
                        <h1 style="color: linear-gradient(to top, #a18cd1 0%, #fbc2eb 100%); font-weight: bold;"> a user just submitted a question that you should review! </h1>
                        <h5>try to answer the question as soon as possible </h5>
                        <h4>Check our website for more detials : <a style="color:blue;">https://academy.fuchicorp.com</a></h4>
                    </center>
                    </body>
                </html>
            """,
                subtype="html",
            )

        else:
            self.msg.add_alternative(txt_template, subtype="html")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(self.email, self.password)
            smtp.send_message(self.msg)


class FrontEndMessage:
    message_date_format = getattr(settings, "DATE_TIME_FORMAT", None)

    def __init__(self, message, expiration=None):
        self.message = message
        self.expiration = expiration

        if expiration is None:
            self.expiration = 3
        self.now = timezone.now()
        self.expire = self.now + timedelta(seconds=self.expiration)

    def is_expired(self):
        self.now = timezone.now()
        return self.expire <= self.now


class GitHubActivitys(models.Model):
    event_type = models.CharField(max_length=20)
    github_name = models.CharField(max_length=20)
    repo_name = models.CharField(max_length=20)
    event_link = models.CharField(max_length=40)
    activity_description = models.TextField(
        max_length=100, blank=True, validators=[MaxLengthValidator(100)]
    )
    evnet_content = models.TextField(
        max_length=15750, blank=True, validators=[MaxLengthValidator(15750)]
    )
    created_date = models.DateTimeField(
        blank=True, null=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST"
    )

    def __str__(self):
        return self.event_type


from main.models import FrontEndMessage

message = FrontEndMessage("Hello World")
message.is_expired()
