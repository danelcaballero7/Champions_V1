from django.urls import path
from Autenticacion.views import VRegistro


urlpatterns = [
    path('', VRegistro.as_view(), name='autenticacion'),

]