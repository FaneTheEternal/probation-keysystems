from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now


class Event(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )

    title = models.CharField(max_length=200)

    allow_wife = models.BooleanField(default=False)
    allow_family = models.BooleanField(default=False)
    for_kids = models.BooleanField(default=False)
    number_of_participants = models.IntegerField(null=True, blank=True)
    event_date = models.DateField(default=now)  # Излишняя полнота имени?
    prepay_date = models.DateField(null=True, blank=True)
    personal_transportation = models.BooleanField(default=False)
    company_transport = models.TextField(null=True, blank=True)
    company_transport_size = models.IntegerField(null=True, blank=True)
    main_price = models.IntegerField(null=True, blank=True)
    other_prices = models.TextField(null=True, blank=True)
    deposit = models.IntegerField(null=True, blank=True)
    some_properties = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("event-detail", args=[str(self.id)])

    class Meta:
        ordering = ['-event_date', 'title']


class Participant(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE)

    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE)

    confirm = models.BooleanField(default=False)

    def __str__(self):
        return '{0} {1}'.format(
            str(self.user.first_name),
            str(self.user.last_name),
        )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'event'],
                name='unique_partic',
            ),
        ]
        unique_together = (('user', 'event'),)
