from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class like(models.Model):
    
    likeid = models.AutoField(primary_key=True)
    liked_by = models.ForeignKey(User , on_delete=models.CASCADE , blank=True , null=True)
    liked_product = models.ForeignKey("structure.products" , on_delete=models.CASCADE , blank=True , null=True)
    liked_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(str(self.liked_by) + str(self.liked_product))