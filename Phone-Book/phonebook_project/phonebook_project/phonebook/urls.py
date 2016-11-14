from django.conf.urls import url
from django.views.generic import TemplateView

from .views import PhonebookView, HomeView

urlpatterns = [
    url(regex=r'^$',
        view=HomeView.as_view(),
        name='phonebook'),
    url(regex=r'^about/$',
        view=TemplateView.as_view(template_name='pages/about.html'),
        name='about'),
    url(regex=r'^new/$',
        view=PhonebookView.new_phonebook,
        name='new_phonebook'),
    url(regex=r'^phonebooks/(\d+)/$',
        view=PhonebookView.as_view(),
        name='view_phonebook'),
    url(regex=r'^phonebooks/(\d+)/add_contact$',
        view=PhonebookView.add_contact,
        name='add_contact'),
    url(regex=r'^phonebooks/(\d+)/edit_contact/(\d+)$',
        view=PhonebookView.edit_contact,
        name='edit_contact'),
    url(regex=r'^phonebooks/([0-9]+)/delete_contact/([0-9]+)$',
        view=PhonebookView.delete_contact,
        name='delete_contact'),
]
