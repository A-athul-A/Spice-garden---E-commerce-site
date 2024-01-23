from django.db import models

# Create your models here.

class Payment_details(models.Model):
    user = models.CharField(max_length = 25)
    address = models.TextField(max_length = 60)
    mobile = models.IntegerField()
    Pin = models.IntegerField()
    products = models.TextField(max_length = 250)
    amount = models.IntegerField()
    pay_method = models.CharField(max_length = 25)
    order_id = models.TextField(max_length = 150)
    o_date = models.CharField(max_length = 25)
    d_date = models.CharField(max_length = 25)
    
    def __str__(self):
        return self.user