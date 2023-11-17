from django.db import models


# Create your models here.

class student(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField(max_length=8)
    age = models.IntegerField()
    gender = models.TextField()
    phno = models.IntegerField()
    email = models.CharField(max_length=250)
    address = models.CharField(max_length=500)
    department = models.CharField(max_length=250)
    courses = models.CharField(max_length=250)
    purposes = models.CharField(max_length=250)
    materials = models.TextField()

    def __str__(self):
        return self.name
