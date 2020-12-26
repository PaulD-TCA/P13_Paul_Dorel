from django import forms

from design.models import Message, Offer

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('title', 'content')

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('offer_title', 'price', 'carriage_price', 'deadline', 'shipment')
