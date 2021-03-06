from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User

from design.models import Message, Offer, Design
from .forms import MessageForm, OfferForm

# Create your views here.
def messages(request):
    """Display the messages page."""
    current_user = request.user.id
    messages_list = Message.objects.filter(
        user_id=current_user) | Message.objects.filter(recipent=current_user)
    template = loader.get_template('community/messages.html')
    context = {'messages_list':messages_list}
    return HttpResponse(template.render(context, request))

def my_offers(request):
    """Display the offers page."""
    current_user = request.user.id
    offer_list = Offer.objects.filter(user_id=current_user).select_related()
    template = loader.get_template('community/my_offers.html')
    context = {'offer_list':offer_list}
    return HttpResponse(template.render(context, request))

def email_user(request, id):
    """Allow user to send an email to another user."""
    if request.method == 'POST':
        current_user = request.user.id
        form = MessageForm(request.POST)
        if form.is_valid():
            message_title = form.cleaned_data['title']
            message_content = form.cleaned_data['content']
            receiver_ref = id
            user = User.objects.get(id=request.user.id)
            data_to_save = Message(recipent=receiver_ref, title=message_title,
                content=message_content, user_id=user)
            data_to_save.save()
            return redirect('messages')
    else:
        form = MessageForm()

    return render(request, 'community/email_to_user.html', {'form':form})

def make_offer(request, id):
    """Allow user to make an offer."""

    if request.method == 'POST':
        current_user = request.user.id
        form = OfferForm(request.POST)
        if form.is_valid():
            offer_title = form.cleaned_data['offer_title']
            offer_price = form.cleaned_data['price']
            offer_carriage_price = form.cleaned_data['carriage_price']
            offer_deadline = form.cleaned_data['deadline']
            offer_shipment = form.cleaned_data['shipment']
            design_ref = id
            user = User.objects.get(id=request.user.id)
            design_ref_id = Design.objects.get(id=design_ref)
            data_to_save = Offer(user_id=user, design_id=design_ref_id,
                offer_title=offer_title, price=offer_price,
                carriage_price=offer_carriage_price, deadline=offer_deadline,
                shipment=offer_shipment)
            data_to_save.save()
            return redirect('my_offers')
    else:
        form = OfferForm()
    return render(request, 'community/make_offer.html', {'form':form})

def offers_on_design(request, id):
    """List all the user offers."""
    current_design = id
    offer_list = Offer.objects.filter(design_id=id)
    template = loader.get_template('community/design_offer.html')
    context = {"offer_list": offer_list}
    return HttpResponse(template.render(context, request))

def delete_message(request):
    """Delete a message."""
    message_to_delete = request.POST.get('messageToDelete')
    Message.objects.filter(id=message_to_delete).delete()
    context = {}
    return HttpResponse("Message have been deleted")

def delete_offer(request):
    """Delete an offer."""
    offer_to_delete = request.POST.get('offerToDelete')
    Offer.objects.filter(id=offer_to_delete).delete()
    context = {}
    return HttpResponse("Message have been deleted")
