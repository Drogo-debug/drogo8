
from django.db import models

class UserFormData(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    account_type = models.CharField(max_length=20)
    debit_card = models.BooleanField(default=False)
    credit_card = models.BooleanField(default=False)
    district = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)

    def __str__(self):
        return self.name

