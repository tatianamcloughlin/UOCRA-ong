from django import forms

from .models import Comentario

class ComentarioForm(forms.ModelForm):

    def init(self, args, **kwargs):
        super().init(args, **kwargs)
        self.fields['comentario'].widget.attrs.update({'rows': '3'})

    class Meta:
        model = Comentario
        fields = ['comentario']
        exclude = ['noticia']