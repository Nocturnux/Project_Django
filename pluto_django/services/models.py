from django.db import models

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=255)
    value= models.CharField(max_length=20)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name