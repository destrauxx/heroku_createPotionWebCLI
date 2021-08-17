from django import forms

from .models import Potion

class CreatePotionModelForm(forms.ModelForm):
    class Meta:
        model = Potion
        fields = [
            'name',
            'ingredients',
            'time',
            'time_plus',
            'time_up_level',
            'up_time',
            'up_level',
            'image',
        ]
