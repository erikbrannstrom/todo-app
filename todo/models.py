from django.db import models

class List(models.Model):
    name = models.CharField(max_length=60)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Item(models.Model):
    list = models.ForeignKey(List)
    description = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.description