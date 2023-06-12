from biomedical.basemodel import TimeBaseModel
from restapi.models.contact_model import Contact
from restapi.models.gender_model import Gender
from django.db import models 


class Patient(TimeBaseModel):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    medical_history = models.TextField()



    def __str__(self):
        return self.name 