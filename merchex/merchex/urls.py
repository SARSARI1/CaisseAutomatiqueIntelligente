# ~/projects/django-web-app/merchex/merchex/urls.py
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('about/', views.about, name="about"),
    path('product/', views.product, name="product"),
    path('client/', views.client, name="client"),
    path('sponsor/', views.sponsor, name="sponsor"),
    path('paiement/', views.paiement, name="paiement"),
    path('error/', views.error, name="error"),
    path('contact/', views.contact, name="contact"),
    path('faq/', views.faq, name="faq"),
    path('feature/', views.feature, name="feature"),
    path('commande/', views.commande, name="commande"),
    path('project/', views.project, name="project"),
    path('service/', views.service, name="service"),
    path('team/', views.team, name="team"),
    path('testimonial/', views.testimonial, name="testimonial"),
    
    
    
]
