from .models import Recipes
from django.forms import ModelForm, TextInput, Textarea


class RecipeForm(ModelForm):
    class Meta:
        model = Recipes
        fields = ["name", "description", "photo", "composition", "method"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
            }),
            "photo": TextInput(attrs={
                'class': 'form-control',
            }),
            "composition": Textarea(attrs={
                'class': 'form-control',
            }),
            "method": Textarea(attrs={
                'class': 'form-control',
            })
        }
