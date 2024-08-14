# ~/projects/django-web-app/merchex/listings/views.py
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect



# Sample view for hello.html
def about(request):
   
    return render(request, 'listings/about.html')
def sponsor(request):
   
    return render(request, 'listings/sponsor.html')

def paiement(request):
   
    return render(request, 'listings/paiement.html')


def commande(request):
   
    return render(request, 'listings/commande.html')

def error(request):
   
    return render(request, 'listings/404.html')
def client(request):
   
    return render(request, 'listings/client.html')
def contact(request):
   
    return render(request, 'listings/contact.html')
def faq(request):
   
    return render(request, 'listings/faq.html')
def feature(request):
   
    return render(request, 'listings/feature.html')
def product(request):
   
    return render(request, 'listings/product.html')
def project(request):
   
    return render(request, 'listings/project.html')
def service(request):
   
    return render(request, 'listings/service.html')
def team(request):
   
    return render(request, 'listings/team.html')
def testimonial(request):
   
    return render(request, 'listings/testimonial.html')

