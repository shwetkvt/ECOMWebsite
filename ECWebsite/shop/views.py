from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index (request):
    return render (request, 'shop/index_old.html')
def about (request):
    return render (request, 'shop/about.html')
def contact (request):
    return render (request, 'shop/contact.html')
def track (request):
    return render (request, 'shop/track.html')
def productview (request):
    return render (request, 'shop/productview.html')
def search (request):
    return render (request, 'shop/search.html')
def checkout (request):
    return render (request, 'shop/checkout.html')