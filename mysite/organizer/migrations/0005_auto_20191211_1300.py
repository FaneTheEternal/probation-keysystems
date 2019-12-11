# Generated by Django 3.0 on 2019-12-11 10:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organizer', '0004_auto_20191211_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='some_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Moder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizer.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]