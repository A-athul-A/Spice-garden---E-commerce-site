from django.db import models

# Create your models here.

class product_tbl(models.Model):
    product_name = models.CharField(max_length=40)
    product_image = models.FileField(upload_to='pictures')
    product_price = models.IntegerField()
    gram_of_product = models.IntegerField(null=True)
    product_description = models.TextField(null=True)
    stock = models.IntegerField(null=True)


    def __str__(self):
        return self.product_name
    