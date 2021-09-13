from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30,verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')
    link = models.URLField(verbose_name='Enlace externo',blank=True,null=True)
    

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'

    def __str__(self):
        return self.title