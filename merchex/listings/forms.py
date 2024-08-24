# ~/projects/django-web-app/merchex/listings/forms.py
from django import forms

from .models import Produit
from .models import Sponsor

class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = ['nom', 'informations_contact', 'site_web', 'logo']
        widgets = {
            'logo': forms.ClearableFileInput(attrs={'multiple': False}),
        }

from django import forms
from .models import Produit

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'categorie', 'prix', 'quantite_stock', 'description', 'image', 'sponsor']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
        }

from django import forms
from .models import Admin

