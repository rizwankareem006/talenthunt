from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class ExtUser(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length = 20, blank=False)
    mobile = models.IntegerField(max_length=10, blank=False)
    dob = models.DateField(blank = False)
    category = models.CharField(max_length = 20, blank=False)

@receiver(post_save,sender = User)
def create_user_extuser(sender, instance, created, **kwargs):
    if created:
        ExtUser.objects.create(username = instance)

@receiver(post_save, sender = User)
def save_user_extuser(sender, instance, **kwargs):
    instance.extuser.save()

