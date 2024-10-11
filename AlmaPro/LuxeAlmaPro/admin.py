from django.contrib import admin
from .models import Utilisateur, Bien, Reservation, Paiement, Avis


# Register your models here.

admin.site.register(Utilisateur)
admin.site.register(Bien)
admin.site.register(Reservation)
admin.site.register(Paiement)
admin.site.register(Avis)
