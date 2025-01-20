from datetime import datetime, date
from django.db import models


class BaseUserInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    alias = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=date.today)

    def __str__(self) -> str:
        return self.alias

    class Meta:
        abstract = True