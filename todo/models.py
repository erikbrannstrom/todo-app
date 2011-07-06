from django.db import models
from django.contrib.auth.models import User

class List(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=60)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Item(models.Model):
    list = models.ForeignKey(List)
    description = models.CharField(max_length=250)
    order = models.PositiveIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def move(self, position):
        if position > self.order:
            for item in Item.objects.filter(order__gt=self.order, order__lte=position, list=self.list):
                item.order -= 1
        elif position < self.order:
            for item in Item.objects.filter(order__lt=self.order, order__gte=position, list=self.list):
                item.order += 1
        self.order = position
        self.save()

    def save(self, *args, **kwargs):
        if self.id == None:
            try:
                self.order = Item.objects.order_by('-order')[0].order + 1
            except IndexError:
                self.order = 1
        super(Item, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.description