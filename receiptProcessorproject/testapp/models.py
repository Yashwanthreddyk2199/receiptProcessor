from django.db import models
import uuid
# Create your models here.


class RetailerReceipt(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    retailer = models.CharField(max_length=100)
    purchaseDate = models.DateField()
    purchaseTime = models.TimeField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.retailer} - {self.purchaseDate} {self.purchaseTime}"


class Item(models.Model):
    receipt = models.ForeignKey(RetailerReceipt, related_name='items', on_delete=models.CASCADE)
    shortDescription = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.shortDescription
