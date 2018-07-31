from django.shortcuts import render
from adventure import models as a_models
# Create your views here.


def home(request):
	safaris = a_models.Safaris.objects.all()
	return render(request,'adventure/temps/home.html',{'saf':safaris})

def safarisdetail(request,safari_id):
	safar = a_models.Safaris.objects.get(pk=safari_id)
	return render(request,'adventure/temps/safari.html',{'safd':safar})

def about(request):
	return render(request,'adventure/temps/about.html')
def practice(request):
	return render(request,'adventure/temps/practice.html')
