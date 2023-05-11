from django.db import models

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    description=models.TextField(max_length=100)
    price=models.IntegerField(max_length=5)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    
