import pdb

from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.forms import formset_factory

from .models import Book, Contact
from .forms import ContactForm, EditContactForm


class PhonebookView(ListView):

    def new_phonebook(request):
        book = Book.books.create_book()
        Contact.objects.create(name=request.POST['name'],
                               phone_number=request.POST['phonenumber'],
                               book=book)
        return redirect('/phonebooks/%d/' % (book.id,))

    def add_contact(request, book_id):
        book = Book.books.get(id=book_id)
        Contact.objects.create(name=request.POST['name'],
                               phone_number=request.POST['phonenumber'],
                               book=book)
        return redirect('/phonebooks/%d/' % (book.id,))

    def edit_contact(request, book_id, contact_id):
        contact = Contact.objects.get(id=contact_id)
        name = [value for key, value in request.POST.items() if 'name' in
                key.lower()][0]
        number = [value for key, value in request.POST.items() if 'phonenumber' in
                  key.lower()][0]
        contact.name = name
        contact.phone_number = number
        contact.save()
        return redirect('/phonebooks/%s/' % (book_id,))

    def delete_contact(request, book_id, contact_id):
        contact = Contact.objects.get(id=contact_id)
        contact.delete()
        return redirect('/phonebooks/%s/' % (book_id,))

    def get(self, request, book_id):
        template_name = 'pages/phonebook.html'
        contact_form = ContactForm()
        book = Book.books.get(id=book_id)
        contact_form.helper.form_action = 'add_contact'

        EditContactFormset = formset_factory(EditContactForm, extra=len(book.contact_set.all()))
        edit_contact_formset = EditContactFormset()

        contacts = book.contact_set.all()
        for i, form in enumerate(edit_contact_formset):
            form.initial = {"name": contacts[i].name,
                            "phonenumber": contacts[i].phone_number}
            form.helper.form_action = 'edit_contact/%d' % contacts[i].id
        # edit_contact_formshelper.form_action = 'add_contact'
        contacts_and_formset = zip(contacts, edit_contact_formset)

        return render(request, template_name,
                      {'contact_form': contact_form,
                       'contacts_and_formset': contacts_and_formset,
                       'book_id': book_id})


class HomeView(TemplateView):

    def get(self, request):
        template_name = 'pages/home.html'
        contact_form = ContactForm()
        contact_form.helper.form_action = 'new_phonebook'
        return render(request, template_name, {'contact_form': contact_form})

