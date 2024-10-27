# Generated by Django 5.1.2 on 2024-10-27 16:39

from django.db import migrations
from api.models import Dispositivo

def criar_dispositivos(apps, schema_editor):
    Dispositivo = apps.get_model('api', 'Dispositivo')
    Dispositivo.objects.create(nome_dispositivo='Android')
    Dispositivo.objects.create(nome_dispositivo='iPhone')

class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(criar_dispositivos),
    ]
