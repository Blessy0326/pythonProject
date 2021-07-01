from django.db import models

# Create your models here.
class userdatainfo(models.Model):
    first_name = models.CharField(max_length = 30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.CharField(max_length=10)
    gender = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.IntegerField()
    Qualification = models.CharField(max_length=30)
    salary = models.IntegerField()
    pannum = models.CharField(max_length=30)
    request_received = models.DateTimeField()

