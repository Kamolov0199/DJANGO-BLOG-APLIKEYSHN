
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('', asosiy),
    path('Mevalar/', Sabzilar),
    path('Sabzilar/',sabzavotlar),
    path('Mevalarr/',Mevalar)
]
