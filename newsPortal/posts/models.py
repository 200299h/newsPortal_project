from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    """ Category table"""
    category_name = models.CharField("Category name", max_length=50)

    def __str__(self):
        return f'{self.category_name}'


class Post(models.Model):
    """ Posts table """
    title = models.CharField("Title", max_length=100)
    text = RichTextField(blank=False)
    date = models.DateTimeField("Date")
    main_category = models.ForeignKey('Category', related_name="main_category", on_delete=models.CASCADE, blank=False)
    category = models.ManyToManyField('Category', related_name="category", blank=True)

    def __str__(self):
        return f'{self.title}'
