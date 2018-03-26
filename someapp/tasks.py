from __future__ import absolute_import, unicode_literals
from celery import shared_task, app
from django.core.mail import send_mail

@shared_task
def task_send_mail(subject, message, from_to, to):
    return send_mail(
        subject,
        message,
        from_to,
        [to],
        fail_silently=False,
    )

@shared_task
def export_excel(resource):
    return resource
