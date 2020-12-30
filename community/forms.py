from django import forms

from design.models import Message, Offer

class MessageForm(forms.ModelForm):
    title = forms.CharField(max_length=50, required=False, help_text='Requis',
        widget=forms.TextInput(attrs={'placeholder': "Titre du message"}))
    content = forms.CharField(max_length=50, required=False, help_text='Requis',
        widget=forms.TextInput(attrs={'placeholder': "Contenu du message"}))
    class Meta:
        model = Message
        fields = ('title', 'content')

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input_button user_btn'


class OfferForm(forms.ModelForm):
    offer_title = forms.CharField(max_length=50, required=False, help_text='Requis',
       widget=forms.TextInput(attrs={'placeholder': "Titre de l'offre"}))
    price = forms.FloatField(required=False, help_text='Requis',
       widget=forms.TextInput(attrs={'placeholder': "Prix proposé en €"}))
    carriage_price = forms.FloatField(required=False, help_text='Requis',
       widget=forms.TextInput(attrs={'placeholder': "Frais de port"}))
    deadline = forms.FloatField(required=False, help_text='Requis',
       widget=forms.TextInput(attrs={'placeholder': "Délais en jours"}))


    class Meta:
        model = Offer
        fields = ('offer_title', 'price', 'carriage_price', 'deadline', 'shipment')

    def __init__(self, *args, **kwargs):
        super(OfferForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'input_button user_btn'
