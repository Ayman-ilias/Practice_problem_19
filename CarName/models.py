from django.db import models
from CompanyName.models import Brand


# Create your models here.
class Car(models.Model):
    car_name = models.CharField(max_length=100)
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)
    launch_date = models.DateField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return self.car_name