from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Contacts(models.Model):
    name = models.CharField(max_length=50)
    number = models.CharField(max_length=25)
    email = models.EmailField()
    message = models.CharField(max_length=600)

    class Meta:
        verbose_name = "Əlaqə forması"
        verbose_name_plural = "Əlaqə formaları"

    def __str__(self):
        return self.email


class News(models.Model):
    title = models.CharField(max_length=100, blank=True)
    title_ru = models.CharField(max_length=100, blank=True)
    title_en = models.CharField(max_length=100, blank=True)
    image = models.ImageField()
    featuredtext = models.CharField(max_length=150)
    featuredtext_ru = models.CharField(max_length=150)
    featuredtext_en = models.CharField(max_length=150)
    body = RichTextUploadingField(config_name="default")
    body_ru = RichTextUploadingField(config_name="default")
    body_en = RichTextUploadingField(config_name="default")


    class Meta:
        verbose_name = "Xəbər"
        verbose_name_plural = "Xəbərlər"
        
    def __str__(self):
        return self.title

class Emails(models.Model):
    emailform = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Email"
        verbose_name_plural = "Emaillər" 

    def __str__(self):
        return self.emailform