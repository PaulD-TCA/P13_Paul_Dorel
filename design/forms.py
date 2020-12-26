from django import forms

from .models import Design

class DesignForm(forms.ModelForm):
    class Meta:
        model = Design
        fields = ('design_name', 'design_image', 'plan_2d','plan_3d', 'assembly_instruction', 'description', 'category')
