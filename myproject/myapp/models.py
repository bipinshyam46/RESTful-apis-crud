from django.db import models

# Create your models here.

class Items(models.Model):
    name=models.TextField(verbose_name='Name')
    price=models.IntegerField(verbose_name='Price')
    description=models.TextField(verbose_name='Description')

    def __str__(self):
        return self.name
