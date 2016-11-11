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


class Child(models.Model):
    name = models.CharField(max_length=50)
    parent = models.CharField(max_length=50)
    age = models.IntegerField()
    pin = models.CharField(unique=True, max_length=4)

    def __str__(self):
        return self.name

    @property
    def status(self):
        return self.checkin_log_set.first()


class CheckIn_Log(models.Model):
    child = models.ForeignKey(Child)
    drop_off = models.DateTimeField(auto_now_add=True)
    pick_up = models.DateTimeField(auto_now=False, null=True)
    in_class = models.BooleanField(default=False)

    class Meta:
        ordering = ('-drop_off',)

    def __str__(self):
        return self.child.name

    @property
    def status_of_child(self):
        if self.in_class is True:
            return str("In Class")
        else:
            return str("Picked Up")

    @property
    def time_in_class(self):
        td = (self.pick_up - self.drop_off)
        return round(((td.seconds / 60) / 60), 3)
