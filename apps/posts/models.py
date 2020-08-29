from django.db import models
from apps.categorias.models import Categoria
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

from PIL import Image
import os


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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.resize_image(self.imagem_post.name, 800)

    @staticmethod
    def resize_image(img_name, new_width):
        img_path = os.path.join(settings.MEDIA_ROOT, img_name)
        img = Image.open(img_path)
        width, height = img.size
        new_height = round((new_width * height) / width)

        new_img = img.resize((new_width, new_height), Image.ANTIALIAS)

        if width <= new_width:
            img.close()
            return

        new_img.save(
            img_path,
            optmize=True,
            quality=60
        )
        new_img.close()