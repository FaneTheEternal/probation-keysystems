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
    )

    title = models.CharField(max_length=200)
