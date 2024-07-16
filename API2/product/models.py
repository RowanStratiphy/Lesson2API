from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.name
