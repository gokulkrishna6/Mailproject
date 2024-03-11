from unicodedata import name
from django.urls import path,include

from AppForm.views import stdform

urlpatterns = [
    path('',stdform,name='stdform')
]