# Generated by Django 3.1.4 on 2021-06-15 23:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20210614_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='catergory',
            field=models.CharField(choices=[('Concerts', 'Concerts'), ('Theater', 'Theater'), ('Kids', 'Kids'), ('Festivals', 'Festivals'), ('Humor', 'Humor')], default=datetime.datetime(2021, 6, 15, 23, 17, 13, 456316, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 6, 15, 23, 17, 25, 610256, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
