# Generated by Django 5.1.2 on 2024-10-27 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_hashtag_postagem_hashtagpostagem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashtagpostagem',
            name='hashtag',
        ),
        migrations.RemoveField(
            model_name='hashtagpostagem',
            name='postagem',
        ),
        migrations.RemoveField(
            model_name='mencao',
            name='postagem',
        ),
        migrations.RemoveField(
            model_name='mencao',
            name='usuario_mencionado',
        ),
        migrations.DeleteModel(
            name='Hashtag',
        ),
        migrations.DeleteModel(
            name='HashtagPostagem',
        ),
        migrations.DeleteModel(
            name='Mencao',
        ),
    ]
