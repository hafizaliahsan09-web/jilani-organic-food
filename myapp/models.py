from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    fathername = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    product = models.CharField(max_length=100)

    QUANTITY_CHOICES = [
        ('250g', '250g'),
        ('500g', '500g'),
        ('1000g', '1000g'),
    ]
    quantity = models.CharField(max_length=10, choices=QUANTITY_CHOICES)

    def __str__(self):
        return self.name
