# Generated by Django 5.1.2 on 2024-10-27 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_repostagem_repostagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='midiarepostagem',
            name='postagem',
        ),
        migrations.RemoveField(
            model_name='repostagem',
            name='dispositivo',
        ),
        migrations.RemoveField(
            model_name='repostagem',
            name='postagem',
        ),
        migrations.RemoveField(
            model_name='repostagem',
            name='repostagem',
        ),
        migrations.RemoveField(
            model_name='repostagem',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='CurtidaRepostagem',
        ),
        migrations.DeleteModel(
            name='MidiaRepostagem',
        ),
        migrations.DeleteModel(
            name='Repostagem',
        ),
    ]
