from django.db import models

# Create your models here.
class Reservation_cabin(models.Model):
    reservation_sale = models.ForeignKey('reservation_sale.Reservation_sale', on_delete=models.DO_NOTHING)
    Cabin = models.ForeignKey('cabin.Cabin', on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=True)