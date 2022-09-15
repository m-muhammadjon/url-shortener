from django.db import models
from django.utils import timezone
import datetime


class User(models.Model):
    uid = models.CharField(max_length=255)

    def __str__(self):
        return f'User with ID {self.uid}'


class Visitor(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'seen at {self.created_at}'


class ShortedLink(models.Model):
    user = models.ForeignKey(User,
                             related_name='links',
                             on_delete=models.SET_NULL,
                             null=True)
    url = models.URLField()
    shorted = models.URLField()
    visitors = models.ManyToManyField(Visitor)

    def get_daily_count(self):
        return self.visitors.filter(created_at__gte=(timezone.now() - datetime.timedelta(days=1))).count()

    def get_weekly_count(self):
        return self.visitors.filter(created_at__gte=(timezone.now() - datetime.timedelta(weeks=1))).count()

    def get_monthly_count(self):
        return self.visitors.filter(created_at__gte=(timezone.now() - datetime.timedelta(days=30))).count()

    def __str__(self):
        return self.shorted
