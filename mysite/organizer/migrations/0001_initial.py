# Generated by Django 3.0 on 2019-12-10 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Event ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirm', models.BooleanField()),
                ('some_custom_data', models.TextField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizer.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_wife', models.BooleanField()),
                ('allow_family', models.BooleanField()),
                ('for_kids', models.BooleanField()),
                ('size', models.IntegerField()),
                ('date', models.DateField(blank=True, null=True)),
                ('prepay_date', models.DateField(blank=True, null=True)),
                ('need_transport', models.BooleanField()),
                ('transport', models.CharField(max_length=200)),
                ('transport_size', models.IntegerField()),
                ('main_price', models.IntegerField()),
                ('other_prices', models.CharField(max_length=200)),
                ('deposit', models.IntegerField()),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='organizer.Event')),
            ],
        ),
    ]
