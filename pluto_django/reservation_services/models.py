from django.db import models

class Reservation_service(models.Model):
    amount = models.IntegerField()
    price = models.IntegerField()
    status = models.BooleanField(default=True)
    reservation_sale = models.ForeignKey('reservation_sale.Reservation_sale', on_delete=models.DO_NOTHING)
    services = models.ForeignKey('services.Services', on_delete=models.DO_NOTHING)



def __str__(self):
    return self.title