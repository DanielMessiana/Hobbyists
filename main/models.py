from django.db import models

class Hobby(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price_range = models.CharField(max_length=100)
    # Add any other relevant fields

    def __str__(self):
        return self.name