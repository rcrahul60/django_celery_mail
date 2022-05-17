from celery import shared_task
from .models import CustomUser
from django.core.mail import send_mail



#send mail task
@shared_task(bind=True)
def sendMailCelery(self):
    users = CustomUser.objects.all()
    for user in users:
        message = 'this is the message'
        mail_subject = "hi celery here"
        to_mail = user.email
        send_mail(
            subject = mail_subject,
            message=message,
            from_email='yourmail@gmail.com',
            recipient_list=[to_mail],
            fail_silently=True
        )
    return 'done'