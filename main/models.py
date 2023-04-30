from django.db import models

class Hobby(models.Model):
    name = models.CharField(max_length=100, default='')
    sport = models.CharField(max_length=100, default='')
    speed = models.CharField(max_length=100, default='')
    intellectual = models.CharField(max_length=100, default='')
    focus = models.CharField(max_length=100, default='')
    social = models.CharField(max_length=100, default='')
    time = models.CharField(max_length=100, default='')
    creative = models.CharField(max_length=100, default='')
    art = models.CharField(max_length=100, default='')
    craft = models.CharField(max_length=100, default='')
    physicalexp = models.CharField(max_length=100, default='')
    cost = models.CharField(max_length=100, default='')
    # Add any other relevant fields

    def __str__(self):
        return self.name