from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=40,verbose_name='Nombre')
    email = models.EmailField(verbose_name='Correo')
    subject = models.TextField(verbose_name='Asunto')
    content = models.URLField(verbose_name='Contenido')
    

    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'

    def __str__(self):
        return self.title