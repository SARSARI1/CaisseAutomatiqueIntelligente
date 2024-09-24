# ~/projects/django-web-app/merchex/merchex/urls.py
from django.contrib import admin
from django.urls import path
from listings import views
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from listings import views 
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name="login"),  # Correct this line
    path('about/', views.about, name="about"),
    path('product/', views.product, name="product"),
    path('client/', views.client, name="client"),
    
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

    path('sponsor/', views.sponsor, name='sponsor'),
    path('add-sponsor/', views.add_sponsor, name='add_sponsor'),
    path('delete-sponsor/', views.delete_sponsor, name='delete_sponsor'),
    path('delete-all-sponsors/', views.delete_all_sponsors, name='delete_all_sponsors'),
    path('edit-sponsor/', views.edit_sponsor, name='edit_sponsor'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-product/', views.edit_product, name='edit_product'),
    path('delete-product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('delete-all-products/', views.delete_all_products, name='delete_all_products'),
    path('clients/add/', views.add_client, name='add_client'),
    path('clients/edit/<int:id>/', views.edit_client, name='edit_client'),
    path('clients/get/<int:id>/', views.get_client_data, name='get_client_data'),
    path('clients/delete/<int:id>/', views.delete_client, name='delete_client'),
    path('clients/delete-all/', views.delete_all_clients, name='delete_all_clients'),
    path('add-sale/', views.add_sale, name='add_sale'),
    path('delete-all-sales/', views.delete_all_sales, name='delete_all_sales'),
    path('admin-management/', views.admin_list, name='admin_list'),
    path('admin-add/', views.add_admin, name='add_admin'),
    path('edit-admin/', views.edit_admin, name='edit_admin'),
    path('delete-admin/', views.delete_admin, name='delete_admin'),
    path('delete-all-admins/', views.delete_all_admins, name='delete_all_admins'),

]
# Add media URL patterns if in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)