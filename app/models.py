from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save


ACCESS_LEVELS = [
    ('e', 'Employee'),
    ('p', 'Parent'),
]


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=2, default='e', choices=ACCESS_LEVELS)

    @property
    def is_employee(self):
        return self.access_level == 'e'


@receiver(post_save, sender="auth.User")
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)

STATUS = {
    ('In', True),
    ('Out', False),
}


class Child(models.Model):
    status = models.BooleanField(default=False, choices=STATUS)
    name = models.CharField(max_length=50)
    parent = models.CharField(max_length=50)
    age = models.IntegerField()
    pin = models.CharField(max_length=4)


class CheckIn_Log(models.Model):
    child = models.ForeignKey(Child)
    drop_off = models.DateTimeField(auto_now_add=True)
    pick_up = models.DateTimeField()
