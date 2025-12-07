from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=100)
    image = models.URLField(max_length=500, blank=True, null=True)
    rating_rate = models.FloatField(default=0.0)
    rating_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
