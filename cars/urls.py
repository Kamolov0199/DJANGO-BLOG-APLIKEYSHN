
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('', Nexia),
    path('Bmw/',  Bmw),
    path('Mers/', Mers),
    path('Rovseroyse/', Rovseroyse),
    path('Ferari/', Ferari),
    path('Tesla/', Tesla),
    path('Bugatti/', Bugatti),
]
