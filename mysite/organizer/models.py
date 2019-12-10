from django.db import models
from django.contrib.auth.models import User
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


class EventOptions(models.Model):
    event = models.OneToOneField(
        "Event",
        on_delete=models.CASCADE
    )

    allow_wife = models.BooleanField()
    allow_family = models.BooleanField()
    for_kids = models.BooleanField()
    size = models.IntegerField()
    date = models.DateField(null=True, blank=True)
    prepay_date = models.DateField(null=True, blank=True)
    need_transport = models.BooleanField()
    transport = models.CharField(max_length=200, null=True, blank=True)
    transport_size = models.IntegerField(null=True, blank=True)
    main_price = models.IntegerField(null=True, blank=True)
    other_prices = models.CharField(max_length=200, null=True, blank=True)
    deposit = models.IntegerField(null=True, blank=True)


class Participant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    confirm = models.BooleanField()
    some_custom_data = models.TextField()
