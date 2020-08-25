from django.db import models
from posts.models import Post
from django.contrib.auth.models import User
from django.utils import timezone


class Comentario(models.Model):
    nome_comentario = models.CharField(verbose_name='Nome', max_length=40)
    email_comentario = models.EmailField(verbose_name='Email')
    comentario_comentario = models.TextField(verbose_name='Comentario')
    post_comentario = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE)
    usuario_comentario = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.DO_NOTHING, null=True, blank=True)
    data_comentario = models.DateTimeField(verbose_name='Data', default=timezone.now)
    publicado_comentario = models.BooleanField(verbose_name='Publicado', default=False)

    def __str__(self):
        return self.nome_comentario
