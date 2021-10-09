from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'foods/index.html')