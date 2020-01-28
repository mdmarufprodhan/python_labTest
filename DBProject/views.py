from django.http import HttpResponse
from django.shortcuts import render

from B1.models import Country


def home(request):
   return render(request, 'home.html')


def showCountry(request):



   allStudents = Country.objects.all()
 #  print(allStudents)


   context = { "allStudents" : allStudents}

   return render(request, 'country.html', context)

 #  return render(request, 'country.html')
