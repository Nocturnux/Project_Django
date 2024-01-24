from django.db import models

# Create your models here.

class Cabin(models.Model):
    image = models.ImageField(upload_to='static/cabin_images', null=True)
    name = models.CharField(max_length=255)
    capacity= models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    typeCabin = models.ForeignKey('typeCabin.TypeCabin', on_delete=models.DO_NOTHING)
    value= models.CharField(max_length=20)


    def __str__(self):
        return self.name