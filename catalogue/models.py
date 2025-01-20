from datetime import date
from django.db import models

from base_model.models import BaseUserInfo


class Author(BaseUserInfo):
    pass


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    category = models.ForeignKey(Category, related_name='related_books', on_delete=models.DO_NOTHING)
    author = models.ForeignKey(Author, related_name='produced_books', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    released_date = models.DateField(default=date.today)

    def __str__(self) -> str:
        return self.name

