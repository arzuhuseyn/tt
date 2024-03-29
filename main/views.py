from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import FormMixin
from .models import Contacts, News
from .forms import ContactForm
from django.views.generic.base import View
from django.utils import translation


def index(request):
    latest_posts = News.objects.order_by('-pk')[0:3]

    context = {
        'latest_posts' : latest_posts,
    }

    return render(request, 'index.html', context=context)


class ContactPageView(FormView):
    form_class = ContactForm
    template_name = "contact.html"
    success_url = "/contact"
    

    def form_valid(self, form):     
        name = form.cleaned_data['name']
        number = form.cleaned_data['number']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
            
        new_contact = Contacts()
        new_contact.name = name
        new_contact.email = email
        new_contact.message = message
        new_contact.number = number
        new_contact.save()
        return super(ContactPageView, self).form_valid(form)

class NewsList(ListView):
    model = News
    template_name = 'news.html'
    paginate_by = 12

class NewsDetail(DetailView):
    model = News
    template_name = 'news_detail.html'


class ActivateLanguageView(View):
    language_code = ''
    redirect_to   = ''

    def get(self, request, *args, **kwargs):
        self.redirect_to   = request.META.get('HTTP_REFERER')
        self.language_code = kwargs.get('language_code')
        translation.activate(self.language_code)
        request.session[translation.LANGUAGE_SESSION_KEY] = self.language_code
        return redirect(self.redirect_to)