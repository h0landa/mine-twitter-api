from django.db import models


class Hashtag(models.Model):
    texto_hashtag = models.TextField()


    def __str__(self):
        return self.texto_hashtag
