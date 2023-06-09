
from django.urls import path
from .views import contact, formulario

urlpatterns = [
    path('', contact, name='contact'),
    path('form/', formulario, name='formulario'),
]
