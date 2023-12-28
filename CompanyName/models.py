from django.db import models

# Create your models here.
class Brand(models.Model):
    brand_name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    car_type = models.CharField(max_length=50)


    def __str__(self):
        return self.brand_name

