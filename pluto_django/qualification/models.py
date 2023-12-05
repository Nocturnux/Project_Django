from django.db import models

class Qualification(models.Model):
    qualification_date = models.DateField()
    score = models.IntegerField()
    status = models.BooleanField(default=True)
    reservation_sale = models.ForeignKey('qualification.Qualification', on_delete=models.DO_NOTHING)



def __str__(self):
    return self.title