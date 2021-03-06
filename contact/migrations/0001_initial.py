# Generated by Django 3.2.6 on 2021-08-30 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Nombre')),
                ('email', models.TextField(verbose_name='Correo')),
                ('subject', models.TextField(verbose_name='Asunto')),
                ('content', models.URLField(verbose_name='Contenido')),
            ],
            options={
                'verbose_name': 'contacto',
                'verbose_name_plural': 'contactos',
            },
        ),
    ]
