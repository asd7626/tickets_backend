# Generated by Django 3.1.4 on 2021-09-09 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_event_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description2',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
