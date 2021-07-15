from django.core.mail import send_mail

from project.celery import app


@app.task
def common(url, to_email, message):
    send_mail(
        "Уведомление",
        message + f"\nClick to watch->{url}",
        'rtluats@gmail.com',
        [to_email],
        fail_silently=False
    )