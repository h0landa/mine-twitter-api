# Generated by Django 5.1.2 on 2024-10-27 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_repostagem_dispositivo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repostagem',
            old_name='texto',
            new_name='texto_repostagem',
        ),
    ]
