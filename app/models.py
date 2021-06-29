from django.db import models
from django.db.models.fields import CharField, DateTimeField, TextField, URLField

# Create your models here.

class Currency(models.Model):
    name = CharField(max_length=25)
    website = URLField(max_length=255)
    added_on = DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.name

class Article(models.Model):
    """news article for crypto currencies copied from other places."""

    title = CharField(max_length=50)
    detail = TextField()
    date = DateTimeField(auto_now=True)
    author = CharField(max_length=25)
    category = CharField(max_length=10)
    image = Image

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        pass


