from django.db import models

# Create your models here.

class SocialUser(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,unique=True)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=500)
    provider=models.CharField(max_length=50)

    def __str__(self):
        return self.name