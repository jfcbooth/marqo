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
        'placeholder': 'Last Nmae'
      }
    ))
    email = forms.CharField(max_length=32, widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'class': 'email',
        'placeholder': 'Email'
      }
    ))

    questions = forms.CharField(max_length=1024, widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        #'class': 'l-field-2',
        'placeholder': 'Ask any questions you have...'
      }
    ))

    class Meta:
      model = Email
      fields = ('first_name', 'last_name', 'email', 'questions')
