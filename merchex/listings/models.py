from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Gestion des utilisateurs (travailleurs) avec reconnaissance faciale
class UtilisateurPersonnalise(AbstractUser):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    donnees_faciales = models.BinaryField(blank=True, null=True)  # Stocker les données de reconnaissance faciale
    numero_telephone = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)

    # Résoudre les conflits en ajoutant related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='utilisateur_personnalise_set',  # Nouveau related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='utilisateur_personnalise_set',  # Nouveau related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return f'{self.nom} {self.prenom}'

# Gestion des clients
class Client(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    numero_telephone = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images_clients/', blank=True, null=True)

    def __str__(self):
        return f'{self.nom} {self.prenom}'

# Gestion des produits
class Produit(models.Model):
    nom = models.CharField(max_length=255)
    categorie = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite_stock = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images_produits/', blank=True, null=True)
    sponsor = models.ForeignKey('Sponsor', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nom

# Gestion des sponsors
class Sponsor(models.Model):
    nom = models.CharField(max_length=255)
    informations_contact = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos_sponsors/', blank=True, null=True)
    site_web = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nom

# Sales Management
class Vente(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='ventes')
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    montant_paye = models.DecimalField(max_digits=10, decimal_places=2)
    monnaie_rendue = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_vente = models.DateTimeField(auto_now_add=True)

    def calculer_monnaie(self):
        return self.montant_paye - self.montant_total

    def __str__(self):
        return f'Vente par {self.client.nom} {self.client.prenom} le {self.date_vente}'

# Tracking Sold Items
class ArticleVendu(models.Model):
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE, related_name='articles')
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)  # Store price at the time of sale

    def __str__(self):
        return f'{self.quantite} x {self.produit.nom} vendu lors de la vente {self.vente.id}'

from django.db import models

class Admin(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # For hashed passwords
    image = models.ImageField(upload_to='images_admins/', blank=True, null=True)

    def __str__(self):
        return f'{self.nom} {self.prenom}'
