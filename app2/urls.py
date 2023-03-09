from app2.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('Sachin/', Sachin, name='Sachin'),
    path('Bumrah/', Bumrah, name='Bumrah'),
    path('Pollard/', Pollard, name='Pollard'),
]