# Generated by Django 3.0 on 2019-12-11 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0008_auto_20191211_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
