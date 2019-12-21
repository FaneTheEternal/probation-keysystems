from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_moderator = models.BooleanField(default=False)

    def __str__(self):
        return '{0} {1}'.format(self.user.first_name, self.user.second_name)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


# Create your models here.
class Event(models.Model):
    owner = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    title = models.CharField(max_length=200)

    allow_wife = models.BooleanField(default=False)
    allow_family = models.BooleanField(default=False)
    for_kids = models.BooleanField(default=False)
    number_of_participants = models.IntegerField(null=True, blank=True)
    event_date = models.DateField(default=now)
    prepay_date = models.DateField(null=True, blank=True)
    personal_transportation = models.BooleanField(default=False)
    company_transport = models.TextField(max_length=200, null=True, blank=True)
    company_transport_size = models.IntegerField(null=True, blank=True)
    main_price = models.IntegerField(null=True, blank=True)
    other_prices = models.CharField(max_length=200, null=True, blank=True)
    deposit = models.IntegerField(null=True, blank=True)
    some_properties = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("event-detail", args=[str(self.id)])

    class Meta:
        ordering = ['event_date']


class Participant(models.Model):
    user = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE)

    event = models.ForeignKey(
        "Event",
        on_delete=models.CASCADE)

    confirm = models.BooleanField()

    def __str__(self):
        return '{0} - {1}'.format(str(self.user), str(self.event))
