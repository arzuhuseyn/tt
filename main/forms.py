from django import forms
from django.forms import Textarea, TextInput
from .models import Contacts, Emails

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = '__all__'
        widgets = { 
            'message' : Textarea(attrs={'cols': 80, 'rows': 20, 'placeholder' : 'Mesaj'}),
            'name' : TextInput(attrs={'placeholder' : 'Adınız'}),
            'email' : TextInput(attrs={'placeholder' : 'E-mail'}),
            'number' : TextInput(attrs={'placeholder' : 'Əlaqə nömrəniz'})
        }

class EmailsForm(forms.ModelForm):
    class Meta:
        model = Emails
        fields = "__all__"