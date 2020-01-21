# Generated by Django 3.0 on 2020-01-21 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('allow_wife', models.BooleanField(default=False)),
                ('allow_family', models.BooleanField(default=False)),
                ('for_kids', models.BooleanField(default=False)),
                ('number_of_participants', models.IntegerField(blank=True, null=True)),
                ('event_date', models.DateField(default=django.utils.timezone.now)),
                ('prepay_date', models.DateField(blank=True, null=True)),
                ('personal_transportation', models.BooleanField(default=False)),
                ('company_transport', models.TextField(blank=True, null=True)),
                ('company_transport_size', models.IntegerField(blank=True, null=True)),
                ('main_price', models.IntegerField(blank=True, null=True)),
                ('other_prices', models.TextField(blank=True, null=True)),
                ('deposit', models.IntegerField(blank=True, null=True)),
                ('some_properties', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-event_date', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confirm', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizer.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='participant',
            constraint=models.UniqueConstraint(fields=('user', 'event'), name='unique_partic'),
        ),
    ]
