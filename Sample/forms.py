from django import forms

from .models import stuform

class studentform(forms.ModelForm):
    class Meta:
        model = stuform
        fields= ['Name']