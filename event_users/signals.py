from django.dispatch import receiver
from django.db.models.signals import post_save,m2m_changed
from django.contrib.auth.models import User,Group
from events.models import Event
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail



@receiver(post_save,sender=User)
def user_activation(sender,instance,created,**kwargs):
    if created:
        
        participant_group=Group.objects.get(name="Participant")
        instance.groups.add(participant_group)
        
        
        
        token=default_token_generator.make_token(instance)
        activation_url=f"{settings.FRONTEND_URL}/user/activate/{instance.id}/{token}"
        subject="Activate Your Account"
        message=f'Hi {instance.username}\n\n Please activate your account by clicking the link below:\n {activation_url}'
        recipient_list=[instance.email]
        try:
            send_mail(subject,message,settings.EMAIL_HOST_USER,recipient_list)
        except Exception as e:
            print(f'Failed to send email to {instance.email} :{str(e)}')
            


@receiver(m2m_changed,sender=Event.Participants.through)
def rsvp_email(sender,instance,action, pk_set,**kwargs):
    if action=='post_add':
        for user_id in pk_set:
            user=instance.Participants.get(id=user_id)
            subject=f"Rsvped Conformed for {instance.name} event"
            message=f"Hi {user.last_name}\n\n You have rsvped for {instance.name} event"
            recipient_list=[user.email]
            send_mail(subject,message,settings.EMAIL_HOST_USER,recipient_list)