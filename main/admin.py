from django.contrib import admin
from .models import Contacts, News, Emails

admin.site.site_header = "TT Fight Club"

admin.site.register(Contacts)
admin.site.register(News)
admin.site.register(Emails)
