from django.db import models

# Create your models here.

class Reservation_sale(models.Model):
    date = models.DateField()
    total = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.BooleanField(default=True)
    customer= models.ForeignKey('Customer.customer', on_delete=models.DO_NOTHING)


def __str__(self):
    return self.title