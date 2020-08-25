from django.db import models
from categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    titulo_post = models.CharField(verbose_name='Titulo', max_length=255)
    autor_post = models.ForeignKey(User, verbose_name='Autor', on_delete=models.DO_NOTHING)
    data_post = models.DateTimeField(verbose_name='Data',default=timezone.now)
    conteudo_post = models.TextField(verbose_name='Conteudo')
    excerto_post = models.TextField(verbose_name='Excerto')
    categoria_post = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.DO_NOTHING,
                                       blank=True, null=True)
    imagem_post = models.ImageField(verbose_name='Imagem', upload_to='post_img/%Y/%m', blank=True, null=True)
    publicado_post = models.BooleanField(verbose_name='Publicado', default=False)

    def __str__(self):
        return self.titulo_post