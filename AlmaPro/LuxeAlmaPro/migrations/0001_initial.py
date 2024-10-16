# Generated by Django 5.1.1 on 2024-10-05 00:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bien',
            fields=[
                ('IDb', models.AutoField(primary_key=True, serialize=False)),
                ('Description', models.TextField()),
                ('Disponibilite', models.JSONField()),
                ('Prix_par_jour', models.DecimalField(decimal_places=2, max_digits=10)),
                ('type_de_bien', models.CharField(choices=[('voiture', 'Voiture'), ('logement', 'Logement'), ('equipement', 'Équipement')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('IDu', models.AutoField(primary_key=True, serialize=False)),
                ('Nom', models.CharField(max_length=50)),
                ('Prenom', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Mot_de_passe', models.CharField(max_length=50)),
                ('Confirmer_votre_mot_de_passe', models.CharField(max_length=50)),
                ('contact', models.CharField(blank=True, max_length=20)),
                ('role', models.CharField(choices=[('proprietaire', 'Propriétaire'), ('locataire', 'Locataire'), ('administrateur', 'Administrateur')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('IDr', models.AutoField(primary_key=True, serialize=False)),
                ('Date_debut', models.DateField()),
                ('Date_fin', models.DateField()),
                ('Statut_du_reservation', models.CharField(choices=[('en_attente', 'En attente'), ('confirmee', 'Confirmée'), ('annulee', 'Annulée')], max_length=20)),
                ('bien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reservations', to='LuxeAlmaPro.bien')),
                ('Locataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Reservations', to='LuxeAlmaPro.utilisateur')),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('IDp', models.AutoField(primary_key=True, serialize=False)),
                ('Montant', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Date_paiement', models.DateField()),
                ('Statut', models.CharField(choices=[('paye', 'Payé'), ('en_attente', 'En attente'), ('echoue', 'Échoué')], max_length=10)),
                ('Reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paiements', to='LuxeAlmaPro.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='Avis',
            fields=[
                ('IDa', models.AutoField(primary_key=True, serialize=False)),
                ('Note', models.IntegerField()),
                ('Commentaire', models.TextField()),
                ('Date_avis', models.DateField()),
                ('Bien', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avis', to='LuxeAlmaPro.bien')),
                ('Utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avis', to='LuxeAlmaPro.utilisateur')),
            ],
        ),
    ]
