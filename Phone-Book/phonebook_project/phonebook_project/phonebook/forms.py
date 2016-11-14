from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ContactForm(forms.Form):
    """ Form for contact """

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('create', 'Create', css_class='btn-primary'))

    name = forms.CharField(label="Name", required=True, max_length=255)
    phonenumber = forms.CharField(label="Phone Number", required=True,
                                  max_length=15)


class EditContactForm(forms.Form):
    """ Form for editing contact """

    def __init__(self, *args, **kwargs):
        super(EditContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('change', 'Change', css_class='btn-primary'))

    name = forms.CharField(label="Name", required=True, max_length=255)
    phonenumber = forms.CharField(label="Phone Number", required=True,
                                  max_length=15)
