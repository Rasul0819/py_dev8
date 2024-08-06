from django.shortcuts import render,get_object_or_404
from . import models
# Create your views here.
def homepage(request):
    books = models.Books.objects.all()
    return render(request,'home.html',{'kitaplar':books})

def product_detail(request,id):
    book = get_object_or_404(models.Books,id=id)
    return render(request,'detail.html',{'book':book})

