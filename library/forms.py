from django import forms
from django.forms import ModelForm
from library.models import BookIns

STATUS = (
    ('m', 'Maintenance'),
    ('o', 'On loan'),
    ('a', 'Available'),
    ('r', 'Reserved'),
)

class ChangeBookModelForm(ModelForm):
    def clean_due_back(self):
       data = self.cleaned_data['due_back']
       return data

    class Meta:
        model = BookIns
        fields = ['renter', 'due_back', 'status']


class ChangeBookForm(forms.Form):
    new_date = forms.DateField()
    change_state = forms.ChoiceField(choices=STATUS)

    def clean_new_date(self):
        data = self.cleaned_data['new_date']
        return data
