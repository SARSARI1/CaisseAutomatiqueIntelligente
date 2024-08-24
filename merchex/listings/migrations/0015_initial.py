# Generated by Django 5.0.7 on 2024-08-13 23:49

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('listings', '0014_delete_agent_delete_band_delete_demande_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('numero_telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('adresse', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('informations_contact', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos_sponsors/')),
                ('site_web', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('categorie', models.CharField(max_length=255)),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantite_stock', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images_produits/')),
                ('sponsor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.sponsor')),
            ],
        ),
        migrations.CreateModel(
            name='UtilisateurPersonnalise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('donnees_faciales', models.BinaryField(blank=True, null=True)),
                ('numero_telephone', models.CharField(blank=True, max_length=20, null=True)),
                ('adresse', models.TextField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='utilisateur_personnalise_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='utilisateur_personnalise_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('montant_paye', models.DecimalField(decimal_places=2, max_digits=10)),
                ('monnaie_rendue', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('date_vente', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ventes', to='listings.client')),
                ('travailleur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.utilisateurpersonnalise')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleVendu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('prix', models.DecimalField(decimal_places=2, max_digits=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles_achetes', to='listings.client')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.produit')),
                ('vente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='listings.vente')),
            ],
        ),
    ]