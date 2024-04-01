from django.db import models



class Profile(models.Model):
    Name=models.CharField(max_length=20)
    Mother=models.CharField(max_length=20)
    Father=models.CharField(max_length=20)
    Phone=models.CharField(max_length=20)
    Email=models.CharField(max_length=20)
    Date_of_birth=models.CharField(max_length=20)
