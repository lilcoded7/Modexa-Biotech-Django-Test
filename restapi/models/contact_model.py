from biomedical.basemodel import TimeBaseModel
from django.db import models


class Contact(TimeBaseModel):
    country_code = models.CharField(max_length=10)
    number = models.IntegerField()

    def __str__(self):
        return self.country_code