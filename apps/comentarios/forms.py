from django.forms import ModelForm

from .models import Comentario


class FormComentario(ModelForm):

    def clean(self):
        data = self.cleaned_data
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('comentario_comentario')

        if len(nome) < 5:
            self.add_error(
                'nome_comentario',
                'O nome precisa ter mais de 5 caracteres.'
            )

        if len(comentario) < 20:
            self.add_error(
                'comentario_comentario',
                'O comentario precisa ter ao menos 20 caracteres.'
            )



    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario_comentario')
