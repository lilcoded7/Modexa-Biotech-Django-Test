from django.urls import path, include
from restapi.views import *
from rest_framework import routers 



router = routers.DefaultRouter()


router.register('register-patient', PatientView)
router.register('crude', PatientWriteView )



urlpatterns = [
    path('v1/', include(router.urls))
]