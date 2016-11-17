from django.test import TestCase

from .models import Entry


class EntryModelTest(TestCase):

    def test_string_representation(self):
        """ Ensure that the entry has a string representation """
        entry = Entry(title="My entry title")
        self.assertEqual(str(entry), "My entry title")

    def test_verbose_name_plural(self):
        self.assertEqual(str(Entry._meta.verbose_name_plural), "entries")
