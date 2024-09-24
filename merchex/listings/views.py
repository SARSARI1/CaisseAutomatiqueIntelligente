# ~/projects/django-web-app/merchex/listings/views.py
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Produit



def about(request):
   
    return render(request, 'listings/about.html')
def sponsor(request):
   
    return render(request, 'listings/sponsor.html')

def login(request):
   
    return render(request, 'listings/login.html')




def commande(request):
   
    return render(request, 'listings/commande.html')

def error(request):
   
    return render(request, 'listings/404.html')

def contact(request):
   
    return render(request, 'listings/contact.html')
def faq(request):
   
    return render(request, 'listings/faq.html')
def feature(request):
   
    return render(request, 'listings/feature.html')

def project(request):
   
    return render(request, 'listings/project.html')
def service(request):
   
    return render(request, 'listings/service.html')
def team(request):
   
    return render(request, 'listings/team.html')
def testimonial(request):
   
    return render(request, 'listings/testimonial.html')

# --------------------------------- views for the sponsor page ------------------------------------
from django.shortcuts import render
from .models import Sponsor
from .forms import SponsorForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Sponsor
from .forms import SponsorForm  # Import if you're using forms

def sponsor(request):
    sponsors = Sponsor.objects.all()
    form = SponsorForm()  # Initialize an empty form
    return render(request, 'listings/sponsor.html', {'sponsors': sponsors, 'form': form})

def add_sponsor(request):
    if request.method == 'POST':
        form = SponsorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sponsor')  # Redirect to the sponsor page to refresh the list
    return redirect('sponsor') 


from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

from django.http import JsonResponse

@require_POST
def edit_sponsor(request):
    sponsor_id = request.POST.get('id')
    sponsor = get_object_or_404(Sponsor, id=sponsor_id)

    sponsor.nom = request.POST.get('nom')
    sponsor.informations_contact = request.POST.get('informations_contact')
    sponsor.site_web = request.POST.get('site_web')

    if 'logo' in request.FILES:
        sponsor.logo = request.FILES['logo']
    sponsor.save()
    
    
    return redirect('sponsor') 
@require_POST
def delete_sponsor(request):
    import json
    data = json.loads(request.body)
    sponsor_id = data.get('id')
    sponsor = get_object_or_404(Sponsor, id=sponsor_id)
    sponsor.delete()
    return redirect('sponsor') 

@require_POST
def delete_all_sponsors(request):
    Sponsor.objects.all().delete()
    return redirect('sponsor') 


# --------------------------------- views for the product page ------------------------------------
from .forms import AddProductForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Produit, Sponsor
from .forms import AddProductForm

def product(request):
    products = Produit.objects.all()  # Fetch all products from the database
    sponsors = Sponsor.objects.all()  # Get all sponsors for the dropdown
    return render(request, 'listings/product.html', {'products': products, 'sponsors': sponsors})

def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produit ajouté avec succès!')
            return redirect('product')  # Redirect to the product view after successful addition
        else:
            messages.error(request, "Une erreur s'est produite lors de l'ajout du produit.")
    else:
        form = AddProductForm()
    
    # Render the form in a modal or a separate page (if needed)
    return render(request, 'listings/product.html', {'form': form})
from django.shortcuts import get_object_or_404, redirect
from .models import Produit  # Make sure you import the correct model

def edit_product(request):
    if request.method == 'POST':
        print("hello i am here in edit product")  # Debugging line to check if the view is called
        product_id = request.POST.get('id')
        product = get_object_or_404(Produit, id=product_id)  # Use Produit instead of Product

        product.nom = request.POST.get('nom')
        product.categorie = request.POST.get('categorie')
        product.prix = request.POST.get('prix')
        product.quantite_stock = request.POST.get('quantite_stock')
        product.description = request.POST.get('description')
        
        if 'image' in request.FILES:
            product.image = request.FILES['image']
        
        if 'sponsor' in request.POST:
            product.sponsor_id = request.POST.get('sponsor')  # Set sponsor_id instead of sponsor

        product.save()

        return redirect('product')  # Make sure 'product' is the correct URL name for redirection
    else:
        return redirect('product')  # Redirect if the request method is not POST

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Produit

def delete_product(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Produit, id=product_id)
        product.delete()
       
    return redirect('product') 

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Produit

@csrf_exempt  # Exempt from CSRF validation if using POST without a form
def delete_all_products(request):
    if request.method == 'POST':
        Produit.objects.all().delete()
    return redirect('product') 


# --------------------------------- views for the client page ------------------------------------
from django.shortcuts import render
from .models import Client

def client(request):
    clients = Client.objects.all()
    return render(request, 'listings/client.html', {'clients': clients})



from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from .models import Client

@require_POST
def add_client(request):
    nom = request.POST.get('nom')
    prenom = request.POST.get('prenom')
    age = request.POST.get('age')
    email = request.POST.get('email')
    numero_telephone = request.POST.get('numero_telephone')
    adresse = request.POST.get('adresse')
    image = request.FILES.get('image')

    Client.objects.create(
        nom=nom,
        prenom=prenom,
        age=age,
        email=email,
        numero_telephone=numero_telephone,
        adresse=adresse,
        image=image
    )
    
    return redirect('client')

from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Client

@require_POST
def edit_client(request, id):
    client = get_object_or_404(Client, id=id)
    
    client.nom = request.POST.get('nom')
    client.prenom = request.POST.get('prenom')
    client.age = request.POST.get('age')
    client.email = request.POST.get('email')
    client.numero_telephone = request.POST.get('numero_telephone')
    client.adresse = request.POST.get('adresse')
    if 'image' in request.FILES:
        client.image = request.FILES['image']
    
    client.save()
    return redirect('client')

# Add a view for loading client data for the modal (optional, if using AJAX)
def get_client_data(request, id):
    client = get_object_or_404(Client, id=id)
    return JsonResponse({
        'id': client.id,
        'nom': client.nom,
        'prenom': client.prenom,
        'age': client.age,
        'email': client.email,
        'numero_telephone': client.numero_telephone,
        'adresse': client.adresse,
        'image': client.image.url if client.image else ''
    })
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import Client

@require_http_methods(["DELETE"])
def delete_client(request, id):
    client = get_object_or_404(Client, id=id)
    client.delete()
    return redirect('client')
@require_http_methods(["DELETE"])
def delete_all_clients(request):
    Client.objects.all().delete()
    return redirect('client')


#------------------------------- Commande ---------------------------------
from django.shortcuts import render
from .models import Vente

   

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Vente, ArticleVendu, Client, Produit
def commande(request):
    ventes = Vente.objects.all().prefetch_related('articles', 'client', 'articles__produit')
    clients = Client.objects.all()
    produits = Produit.objects.all()
    return render(request, 'listings/commande.html', {'ventes': ventes,'clients': clients,
        'produits': produits})

@require_POST
def add_sale(request):
    client_id = request.POST.get('client_id')
    montant_total = request.POST.get('montant_total')
    montant_paye = request.POST.get('montant_paye')
    
    # Create the Vente instance
    vente = Vente.objects.create(
        client_id=client_id,
        montant_total=montant_total,
        montant_paye=montant_paye,
        monnaie_rendue=float(montant_paye) - float(montant_total)
    )
    
    # Add the sold products
    produits_ids = request.POST.getlist('produit_id[]')
    quantites = request.POST.getlist('quantite[]')
    prix = request.POST.getlist('prix[]')

    for produit_id, quantite, prix_unitaire in zip(produits_ids, quantites, prix):
        ArticleVendu.objects.create(
            vente=vente,
            produit_id=produit_id,
            quantite=quantite,
            prix=prix_unitaire
        )

    return redirect("commande")


    from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Vente

@require_POST
def delete_all_sales(request):
    # Check for CSRF token in the request
    if request.method == 'POST':
        Vente.objects.all().delete()  # Delete all sales
    
    return redirect("commande")




#------------------------------  admin views -----------------------
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Admin
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Admin
 

def admin_list(request):
    admins = Admin.objects.all()
    return render(request, 'listings/admin.html', {'admins': admins})
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Admin
from django.contrib.auth.hashers import make_password
def add_admin(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image = request.FILES.get('image')

        # Hasher le mot de passe avant de sauvegarder
        hashed_password = make_password(password)

        # Créer et sauvegarder le nouvel admin
        admin = Admin(nom=nom, prenom=prenom, email=email, password=hashed_password, image=image)
        admin.save()

        messages.success(request, 'Administrateur ajouté avec succès!')
        return redirect('admin_list')

    return render(request, 'listings/admin.html')

def edit_admin(request):
    if request.method == 'POST':
        admin_id = request.POST.get('admin_id')
        admin = get_object_or_404(Admin, id=admin_id)
        
        admin.nom = request.POST.get('nom')
        admin.prenom = request.POST.get('prenom')
        admin.email = request.POST.get('email')
        if request.POST.get('password'):
            admin.password = request.POST.get('password')  # N'oubliez pas de hasher le mot de passe
        if request.FILES.get('image'):
            admin.image = request.FILES.get('image')
        
        admin.save()
        messages.success(request, 'Administrateur mis à jour avec succès!')
        return redirect('admin_list')

def delete_admin(request):
    if request.method == 'POST':
        admin_id = request.POST.get('admin_id')
        admin = get_object_or_404(Admin, id=admin_id)
        admin.delete()
        messages.success(request, 'Administrateur supprimé avec succès!')
        return redirect('admin_list')

def delete_all_admins(request):
    if request.method == 'POST':
        Admin.objects.all().delete()
        messages.success(request, 'Tous les enregistrements administratifs ont été supprimés avec succès!')
        return redirect('admin_list')



#--------------------------------- paiment pages -----------------------------------------------------

def paiement(request):
    produits = Produit.objects.all()
    clients = Client.objects.all()
    
    context = {
        'produits': produits,
        'clients': clients,
    }
   
    return render(request, 'listings/paiement.html',context)


#-------------------------------------------------------- Login page traitement --------------------------------

import cv2
import numpy as np
import face_recognition
import os

# Load images from the database (folder path)
path = 'media/images_admins'
images = []
classNames = []
personsList = os.listdir(path)

# Load and store images and corresponding class names
for cl in personsList:
    curPersonn = cv2.imread(f'{path}/{cl}')
    images.append(curPersonn)
    classNames.append(os.path.splitext(cl)[0])

# Function to encode images
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

# Encode known images
encodeListKnown = findEncodings(images)
print('Encoding Complete')

# Function to compare a given image to the known database
def compare_image_to_database(image_path):
    # Load the image taken from the browser
    img = cv2.imread(image_path)
    
    # Resize the image and convert to RGB
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Find face locations and encodings in the image
    faceCurentFrame = face_recognition.face_locations(imgS)
    encodeCurentFrame = face_recognition.face_encodings(imgS, faceCurentFrame)

    # If no face is detected, return False
    if not encodeCurentFrame:
        return False

    # Compare the detected face to known encodings
    for encodeFace in encodeCurentFrame:
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        # Find the best match index
        matchIndex = np.argmin(faceDis)

        # Return True if a match is found
        if matches[matchIndex]:
            return True
            

    return False


from listings.models import Admin  # Adjust the import based on your app structure

def check_admin_credentials(email, password):
    try:
        # Query the Admin model to check if an admin with the given nom and password exists
        admin = Admin.objects.get(email=email, password=password)
        return True
    except Admin.DoesNotExist:
        return False

#--------------------------------- Verfication of credentials -------------------------------------
#getting user entrey : image , email , password
from django.contrib import messages
import os
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

import base64  # Add this line

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        image_data = request.POST.get('image')

        # Step 1: Convert the base64 image data to an image file
        if image_data:
            # Extract the base64 string (remove "data:image/png;base64," prefix)
            image_data = image_data.split(',')[1]

            # Decode the base64 string into binary data
            image_binary = base64.b64decode(image_data)

            # Save the image temporarily
            image_path = os.path.join(settings.MEDIA_ROOT, 'temp_face_image.png')
            with open(image_path, 'wb') as f:
                f.write(image_binary)

            # Step 2: Handle image verification
            if not compare_image_to_database(image_path):
                # If image verification fails, remove temp image and add an error message
                os.remove(image_path)  # Clean up the temporary file
                messages.error(request, "Votre visage n'a pas été reconnu.")
                return redirect('login')  # Redirect to the login page

            # Step 3: Handle credentials if image is verified
            os.remove(image_path)  # Clean up the temporary file after verification

            if check_admin_credentials(email, password):
                # If credentials are correct, redirect to payment page
                return redirect('paiement')  # Redirect to the payment page
            else:
                # If credentials are incorrect, add an error message
                messages.error(request, 'Identifiants incorrects.')
                return redirect('login')  # Redirect to the login page

    # Default behavior: render login page if not a POST request
    return render(request, 'listings/login.html')
