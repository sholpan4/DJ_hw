from django.forms import ModelForm
from .models import Film


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ('title', 'content', 'year', 'genre')