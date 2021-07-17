from django.db import models


class Event(models.Model):
    CITIES = [('dnipro', 'dnipro'), ('kyiv', 'kyiv'), ('kharkiv', 'kharkiv')]
    CATEGORIES = [('concerts','concerts'), ('theater', 'theater'),('kids','kids'), ('festivals', 'festivals'), ('humor', 'humor')]

    poster = models.URLField()
    headliner = models.CharField(max_length=100)
    city = models.CharField(max_length=100, choices=CITIES)
    address = models.TextField(default='')
    date = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=300)
    category = models.CharField(max_length=100, choices=CATEGORIES)
    date_added = models.DateTimeField(auto_now_add=True)
    popular = models.BooleanField(default=False)
    carousel = models.BooleanField(default=False)

    class Meta:
        ordering = ['date']
    
    def __str__(self):
        return self.headliner + ' | ' + self.city + ' | ' + str(self.date.strftime('%d %B, %H:%M')) + ' | ' + self.category


