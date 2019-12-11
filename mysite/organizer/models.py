from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid


# Create your models here.
class Event(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text='Event ID',
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    title = models.CharField(max_length=200)

    allow_wife = models.BooleanField(default=False)
    allow_family = models.BooleanField(default=False)
    for_kids = models.BooleanField(default=False)
    size = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    prepay_date = models.DateField(null=True, blank=True)
    need_transport = models.BooleanField(default=False)
    transport = models.CharField(max_length=200, null=True, blank=True)
    transport_size = models.IntegerField(null=True, blank=True)
    main_price = models.IntegerField(null=True, blank=True)
    other_prices = models.CharField(max_length=200, null=True, blank=True)
    deposit = models.IntegerField(null=True, blank=True)
    some_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return '{0} ({1})'.format(self.id, self.title)

    def get_absolute_url(self):
        return reverse("event-detail", kwargs={"pk": self.id})

    class Meta:
        ordering = ['date']


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    confirm = models.BooleanField()
    some_custom_data = models.TextField()

    def __str__(self):
        return '{0} - {1}'.format(str(self.user), str(self.event))


class Moder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
