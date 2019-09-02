from django.urls import path, include
from . import views
from django.conf.urls import url
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.index, name="index"),
    path('telimciler', TemplateView.as_view(template_name="telimciler.html"), name="telimciler"),
    path('heftelik', TemplateView.as_view(template_name="heftelik.html"), name="heftelik"),
    path('news', views.NewsList.as_view(), name="news"),
    path('news/<int:pk>', views.NewsDetail.as_view(), name="news-detail"),
    path('contact', views.ContactPageView.as_view(), name="contact"),
    path('language/activate/<language_code>/', views.ActivateLanguageView.as_view(), name='activate_language'),
]