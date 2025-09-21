from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    
    CATEGORY_CHOICES = [
        ('apparel & gear', 'Apparel & Gear'),
        ('equipment', 'Equipment'),
        ('accessories', 'Accessories'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=20, default='unnamed product')
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='equipment')
    is_featured = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name

    