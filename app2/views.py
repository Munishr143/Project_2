from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Sachin(request):
    return HttpResponse('<h2>He is the God Of Cricket</h2>')

def Bumrah(request):
    return HttpResponse("He is the World's No.1 Bowler")

def Pollard(request):
    return HttpResponse('He is the Hard_Hitter')