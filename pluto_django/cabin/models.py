from django.db import models

# Create your models here.

class Cabin(models.Model):
    name = models.CharField(max_length=255)
    capacity= models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    typeCabin = models.ForeignKey('typeCabin.TypeCabin', on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.name