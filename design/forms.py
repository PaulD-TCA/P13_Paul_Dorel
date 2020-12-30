from django import forms

from .models import Design

class DesignForm(forms.ModelForm):
    design_name = forms.CharField(max_length=30, required=False, help_text='Requis',
    widget=forms.TextInput(attrs={'placeholder': "Nom du design"}))
    description = forms.CharField(max_length=30, required=False, help_text='Requis',
    widget=forms.TextInput(attrs={'placeholder': "Description"}))

    class Meta:
        model = Design
        fields = ('design_name', 'design_image', 'plan_2d','plan_3d',
            'assembly_instruction', 'description', 'category')

class NameForm(forms.Form):
    your_name = forms.CharField(max_length=100)
