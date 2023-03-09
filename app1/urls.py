from app1.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('MSD/', MSD, name='MSD'),
    path('Raina/', Raina, name='Raina'),
    path('Jaddu/', Jaddu, name='Jaddu'),
]