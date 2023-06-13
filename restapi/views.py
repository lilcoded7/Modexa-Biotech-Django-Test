from django.shortcuts import render
from restapi.serializers import PatientSerializer
from rest_framework import mixins, viewsets, generics
from rest_framework.response import Response 
from restapi.models.patient_model import Patient 
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.


class PatientView(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin
    ):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [AllowAny]


class PatientWriteView(
    viewsets.GenericViewSet, 
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
    ):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
 