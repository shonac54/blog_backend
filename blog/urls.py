from django.urls import path,include
from . import views

urlpatterns = [
   path('adduser/',views.userRegister, name='adduser')
]
