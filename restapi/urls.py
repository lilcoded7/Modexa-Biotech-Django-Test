from django.urls import path, include
from restapi.views import *
from rest_framework import routers 



router = routers.DefaultRouter()


router.register('patient', PatientView)
router.register('update/delete', PatientWriteView )



urlpatterns = [
    path('', include(router.urls))
]