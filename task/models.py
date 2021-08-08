from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



REPEAT_TYPE= [
    ('repetition', 'Repetition'),
    ('frequency', 'Frequency'),
    ]

WEEKDAYS =(
    ('sun','SUN'),
    ('mon','MON'),
    ('tue','TUE'),
    ('wed','WED'),
    ('thu','THU'),
    ('fri','FRI'),
    ('sat','SAT'),
)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, default='')
    start_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    repeat_type = models.CharField(choices=REPEAT_TYPE, max_length=100)
    weekdays = models.CharField(choices=WEEKDAYS, max_length=100)

    def __str__(self):
        return self.email


