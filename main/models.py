from django.db import models

# Create your models here.
class Product(models.Model):
    
    CATEGORY_CHOICES = [
        ('apparel & gear', 'Apparel & Gear'),
        ('equipment', 'Equipment'),
        ('accessories', 'Accessories'),
    ]
    
    name = models.CharField(max_length=20, default='unnamed product')
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='equipment')
    is_featured = models.BooleanField(default=False)
    stock = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name