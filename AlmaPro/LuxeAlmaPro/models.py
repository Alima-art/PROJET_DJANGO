from django.db import models
import datetime
from django.utils import timezone
# Ce fichier permet la gestion des classes possibles. Voici nos 5 classes

# creation de la classe pour le model utilisateur


class Utilisateur(models.Model):
    # Les propritées du model utilisateur
    IDu = models.AutoField(primary_key=True)
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)
    Mot_de_passe = models.CharField(max_length=50)
    Confirmer_votre_mot_de_passe = models.CharField(max_length=50)
    contact = models.CharField(max_length=20, blank=True)
    ROLE_CHOICES = [
        ('proprietaire', 'Propriétaire'),
        ('locataire', 'Locataire'),
        ('administrateur', 'Administrateur'),
    ]
    # Rôle de l'utilisateur
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)

    def __str__(self):
        return self.Utilisateur_text


# creation de la classe pour le model bien
class Bien(models.Model):
    # Les propritées du model biens
    IDb = models.AutoField(primary_key=True)
    Description = models.TextField()
    Disponibilite = models.JSONField()
    Prix_par_jour = models.DecimalField(max_digits=10, decimal_places=2)
    TYPE_CHOICES = [
        ('voiture', 'Voiture'),
        ('logement', 'Logement'),
        ('equipement', 'Équipement'),
        ('autre', 'Autre'),
    ]
    Type_de_bien = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.Type_de_bien} - {self.Description[:20]}"


# creation de la classe pour le model reservation
class Reservation(models.Model):
    # Les propritées du model Reservation
    IDr = models.AutoField(primary_key=True)
    # Référence au bien réservé
    bien = models.ForeignKey(
        Bien, on_delete=models.CASCADE, related_name='Reservations')
    # Référence à l'utilisateur locataire
    Locataire = models.ForeignKey(
        Utilisateur, on_delete=models.CASCADE, related_name='Reservations')
    Date_debut = models.DateField()
    Date_fin = models.DateField()
    Statut = [
        ('en_attente', 'En attente'),
        ('confirmee', 'Confirmée'),
        ('annulee', 'Annulée'),
    ]
    # Statut de la réservation
    Statut_du_reservation = models.CharField(max_length=20, choices=Statut)

    def __str__(self):
        return f"Réservation {self.IDr} - {self.Bien}"


# creation de la classe pour le model  paeiment
class Paiement(models.Model):
    # Les propritées du model paeiment
    IDp = models.AutoField(primary_key=True)
    # Référence à la réservation
    Reservation = models.ForeignKey(
        Reservation, on_delete=models.CASCADE, related_name='paiements')
    Montant = models.DecimalField(max_digits=10, decimal_places=2)
    Date_paiement = models.DateField()
    Statut_du_paeiment = [
        ('paye', 'Payé'),
        ('en_attente', 'En attente'),
        ('echoue', 'Échoué'),
    ]
    Statut = models.CharField(max_length=10, choices=Statut_du_paeiment)

    def __str__(self):
        return f"Paiements {self.IDp} - {self.Montant}"


# creation de la classe pour le model avis des clients
class Avis(models.Model):
    # Identifiant unique de l'avis
    IDa = models.AutoField(primary_key=True)
    # Référence au bien évalué
    Bien = models.ForeignKey(
        Bien, on_delete=models.CASCADE, related_name='avis')
    # Référence à l'utilisateur ayant laissé l'avis
    Utilisateur = models.ForeignKey(
        Utilisateur, on_delete=models.CASCADE, related_name='avis')
    Note = models.IntegerField()
    Commentaire = models.TextField()
    Date_avis = models.DateField()

    def __str__(self):
        return f"Avis {self.IDa} - {self.Note}/5"

    def was_published_recently(self):
        return self. Date_avis >= timezone.now() - datetime.timedelta(days=1)
