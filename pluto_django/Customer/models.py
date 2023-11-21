from django.db import models

class customer(models.Model):
    name = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    document = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=255)
    cellphone = models.CharField(max_length=20)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

# Create your models here.
