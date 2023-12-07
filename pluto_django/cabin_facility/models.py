from django.db import models

# Create your models here.
class Cabin_facility(models.Model):
    idCabin = models.ForeignKey('cabin.Cabin', on_delete=models.DO_NOTHING)
    idFacilities = models.ForeignKey('facilities.Facilities', on_delete=models.DO_NOTHING)
    amount = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    