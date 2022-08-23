from django.db import models
from django.contrib.auth.models import User

class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now=False)
    wash_type = models.IntegerField()
    booking_time = models.TimeField(auto_now_add=False)
    collection_time = models.TimeField(auto_now=False, null=True, blank=True)

    # def __str__(self):
    #     return self.booking_time
