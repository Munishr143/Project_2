from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def MSD(request):
    return HttpResponse('<h1>He is the Best Finisher in the World</h1>')

def Raina(request):
    return HttpResponse('He is called as Mr.Ipl or Chinna_Thala')

def Jaddu(request):
    return HttpResponse('He is best All_Rounder')