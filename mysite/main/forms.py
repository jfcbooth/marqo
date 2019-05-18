from django import forms
from main.models import Email

class EmailForm(forms.ModelForm):
    first_name = forms.CharField(max_length=32, widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'class': 'l-field',
        'placeholder': 'First Name'
      }
    ))
    last_name = forms.CharField(max_length=32, widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'class': 'l-field',
        'placeholder': 'Last Name'
      }
    ))
    email = forms.CharField(max_length=32, widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'class': 'l-field-2',
        'placeholder': 'Email'
      }
    ))
    class Meta:
      model = Email
      fields = ('first_name', 'last_name', 'email')