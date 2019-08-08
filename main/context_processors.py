from .models import Emails
from .forms import EmailsForm

def emailsform(request):
    form_class = EmailsForm
    form = form_class(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['emailform']   
            new_contact = Emails()
            new_contact.emailform = email
            new_contact.save()
        else:
            form = EmailsForm()

    return {'form':form}