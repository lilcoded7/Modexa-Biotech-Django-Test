from biomedical.basemodel import TimeBaseModel
from django.db import models 


class Patient(TimeBaseModel):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    contact = models.CharField(max_length=100, null=True, blank=True)
    medical_history = models.TextField()


    def __str__(self):
        return self.name 