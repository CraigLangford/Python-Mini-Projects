from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Book(models.Model):
    text = models.TextField(default='')
    pass

class Contact(models.Model):
    first_name = models.TextField(default='', max_length=255)
    last_name = models.TextField(default='', max_length=255)
    phone_number = PhoneNumberField()
    book = models.ForeignKey(Book, default='')
