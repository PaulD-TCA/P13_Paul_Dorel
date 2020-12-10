from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False, help_text='Requis', widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
    email = forms.EmailField(max_length=254, help_text='Requis', widget=forms.TextInput(attrs={'placeholder': 'email'}))
    password1 = forms.CharField(max_length=254, help_text='Requis', widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))
    password2 = forms.CharField(max_length=254, help_text='Requis', widget=forms.PasswordInput(attrs={'placeholder': 'Confirmez le mot de passe'}))#, widget=forms.TextInput(attrs={'placeholder': 'Confirmez le mot de passe'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input_button user_btn'
