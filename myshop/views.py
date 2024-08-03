from django.shortcuts import render
from . import models
# Create your views here.
def homepage(request):
    books = models.Books.objects.all()
    return render(request,'home.html',{'kitaplar':books})