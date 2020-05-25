from django.db import models

# Create your models here.
class FlightDepartCode(models.Model):
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.code

    # class Meta:
    #     verbose_name_plural = 'codes'

class FlightArriveCode(models.Model):
    arrive_code = models.CharField(max_length=3)

    def __str__(self):
        return self.arrive_code