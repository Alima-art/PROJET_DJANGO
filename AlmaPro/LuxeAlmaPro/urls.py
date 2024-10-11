from django.urls import path
from .views import register, connexion, inscrire, home, nous


urlpatterns = [
    # path('', index, name="index"),
    path('', home, name="home"),
    path('', connexion, name="connexion"),
    path('', register, name="register"),
    path('', inscrire, name="inscrire"),
    path('', nous, name="nous"),
]
