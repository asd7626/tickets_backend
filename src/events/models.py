from django.db import models
from datetime import date, datetime
from django.utils.text import slugify
from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

class Event(models.Model):
    CITIES = [('dnipro', 'dnipro'), ('kyiv', 'kyiv'), ('kharkiv', 'kharkiv')]
    CATEGORIES = [('concerts','concerts'), ('theater', 'theater'),('kids','kids'), ('festivals', 'festivals'), ('humor', 'humor')]
    MONTHS = [('january', 'january'), ('february', 'february'), ('march', 'march'), ('april', 'april'), ('may', 'may'), ('june', 'june'), ('july', 'july'), ('august', 'august'), ('september', 'september'), ('october', 'october'),('november', 'november'),('december', 'december')]
    poster = models.URLField()
    headliner = models.CharField(max_length=100)
    city = models.CharField(max_length=100, choices=CITIES)
    address = models.TextField(default='')
    date = models.DateTimeField()
    month = models.CharField(max_length=100, choices=MONTHS, default='january')
    description = models.TextField(null=True, blank=True)
    description2 = models.TextField(null=True, blank=True, default='')
    price = models.IntegerField(default=300)
    category = models.CharField(max_length=100, choices=CATEGORIES)
    date_added = models.DateTimeField(auto_now_add=True)
    popular = models.BooleanField(default=False)
    carousel = models.BooleanField(default=False)
    

    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return self.headliner + ' | ' + self.city + ' | ' + str(self.date.strftime('%d %B, %H:%M')) + ' | ' + self.category



class SubscribeEmail(models.Model):
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email


class Order(models.Model):
    events = models.ManyToManyField(Event)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    total = models.IntegerField(default=1)
    comment = models.TextField(default='', null=True, blank=True)

    def __str__(self):
        return str(self.id) 





@receiver(post_save, sender=SubscribeEmail)
def sending_email_subscribe(sender, instance, **kwargs):
    send_mail(
    'Tickets UA',
    'Congratulations. You have subscribed to receiving latest updates from our site!',
    'TICKETS UA',
    [str(instance.email)],
    fail_silently=False,
    )
    print('Email sent')


@receiver(post_save, sender=Order)
def sending_email_order(sender, instance, **kwargs):
    events = '\n \n'
    for event in instance.events.all():
        events+= '{} in {} on {} at {} \n'.format(event.headliner.upper(), event.city.capitalize(), event.date.strftime("%d %B"), event.date.strftime("%H:%M"))
    #events = ["{} in {} on {}".format(event.headliner, event.city.capitalize(), event.date.date()) for event in instance.events.all()]
    if len(instance.events.all()) > 0:
        send_mail(
            'Tickets UA',
            'Hello, {}. Here is your order confirmation. You ordered {} tickets: {} \nTotal: ${}'.format(instance.name, len(instance.events.all()), events, instance.total),
            'TICKETS UA',
            [str(instance.email)],
            fail_silently=False
        )
        print('Order sent')