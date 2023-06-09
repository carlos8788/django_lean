from django.db import models

# Create your models here.
class Contacto(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=False)
    comentario = models.TextField(blank=True)

    def __str__(self):
        return self.email