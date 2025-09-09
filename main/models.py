from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=20, default='unnamed product')
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField()
    is_featured = models.BooleanField()
    
    def __str__(self):
        return self.name