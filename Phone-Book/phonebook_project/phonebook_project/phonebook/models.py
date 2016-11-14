from django.db import models


class BookManager(models.Manager):
    def create_book(self):
        book = self.create()
        return book


class Book(models.Model):
    books = BookManager()


class Contact(models.Model):
    name = models.TextField(default='', max_length=255)
    phone_number = models.TextField(default='', max_length=15)
    book = models.ForeignKey(Book, default='')
