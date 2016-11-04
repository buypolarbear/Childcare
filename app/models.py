from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


# ACCESS_LEVELS = [
#     ('e', 'Employee'),
#     ('p', 'Parent'),
# ]

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    # access_level = models.CharField(max_length=2, default='p', choices=ACCESS_LEVELS)


@receiver(post_save, sender="auth.User")
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)


class Child(models.Model):
    in_class = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    parent = models.CharField(max_length=50)
    age = models.IntegerField()
    pin = models.CharField(max_length=4)
