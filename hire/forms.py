from django import forms
from .models import Commition


class CommitionForm(forms.ModelForm):

    class Meta:
        model = Commition
        fields = (
            'yourname', 'cover', 'colour', 'setting', 'number_of_characters',
            'number_of_pages', 'deadline', 'email',
        )
