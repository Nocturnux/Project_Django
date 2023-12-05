from django.db import models

class Payment(models.Model):
    payment_date = models.DateField()
    price = models.IntegerField()
    status = models.BooleanField(default=True)
    reservation_sale = models.ForeignKey('reservation_sale.Reservation_sale', on_delete=models.DO_NOTHING)



def __str__(self):
    return self.title
