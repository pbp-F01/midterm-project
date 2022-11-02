from django.forms import ModelForm
from berita.models import CommentModel

class CommentForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = ['comments_substance',]