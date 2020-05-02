from userprofiles.api.views import Register, UserLoginAPIView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
app_name = 'user_api'

urlpatterns = [
    path('signup/',Register.as_view(), name='registration'),
    path('login/',UserLoginAPIView.as_view(), name='login'),
]
