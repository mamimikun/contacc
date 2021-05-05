from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Contact(models.Model):
    # only text. add validation
    name = models.CharField(blank=False, max_length=70)
    # only text. add validation
    lastname = models.CharField(blank=False, max_length=70)
    # company is alphanumeric. add validation
    company = models.CharField(blank=True, max_length=70)
    # phone number is unique
    phone_number = PhoneNumberField(null=True, blank=True, unique=True)
    email = models.EmailField(unique=True)
