from django.urls import path
from . import views 

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




urlpatterns = [
    path('register/', views.CreateUser.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')


]