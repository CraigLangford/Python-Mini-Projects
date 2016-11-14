from django.test import TestCase
from django.core.urlresolvers import resolve

from .models import Book, Contact

class TableAndItemsModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        book = Book()
        book.save()

        first_contact = Contact()
        first_contact.first_name = "Charlie"
        first_contact.last_name = "Chaplin"
        first_contact.phone_number = "+337312345678"
        first_contact.book = book
        first_contact.save()
    
        saved_book = Book.objects.first()
        self.assertEqual(saved_book, book)

        second_contact = Contact()
        second_contact.first_name = "Chelsea"
        second_contact.last_name = "Football"
        second_contact.phone_number = "+331232345678"
        second_contact.book = book
        second_contact.save()

        saved_contacts = Contact.objects.all()
        self.assertEqual(saved_contacts.count(), 2)

        first_saved_contact = saved_contacts[0]
        second_saved_contact = saved_contacts[1]
        self.assertEqual(first_saved_contact.first_name, "Charlie")
        self.assertEqual(first_saved_contact.book, book)
        self.assertEqual(second_saved_contact.phone_number, "+331232345678")
        self.assertEqual(second_saved_contact.book, book)
        
class PhonebookViewTest(TestCase):

