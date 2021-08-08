from django.urls import path
from .views import SignUpView, ProfileView
from . import views


urlpatterns = [
    path('', SignUpView.as_view(), name='signup'),
    path('login/fillform/',views.ProfileView, name='fillform'),
    path('login/result/',views.Result, name='result'),
]