# Generated by Django 3.1.4 on 2021-09-15 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0028_order_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
