from biomedical.basemodel import TimeBaseModel
from restapi.models.gender_model import Gender
from django.db import models 


class Patient(TimeBaseModel):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    contact = models.CharField(max_length=100, null=True, blank=True)
    medical_history = models.TextField()



    def __str__(self):
        return self.name 