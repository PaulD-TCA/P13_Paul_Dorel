from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User

from design.models import Message, Offer, Design
from .forms import MessageForm, OfferForm

# Create your views here.
def messages(request):
    """Display the main web page."""
    current_user = request.user.id
    messages_list = Message.objects.filter(user_id=current_user)
    template = loader.get_template('community/messages.html')
    context = {'messages_list':messages_list}
    return HttpResponse(template.render(context, request))

def my_offers(request):
    """Display the main web page."""
    current_user = request.user.id
    # offer_list = Offer.objects.select_related('design_id', 'user_id').filter(user_id=current_user)
    offer_list = Offer.objects.filter(user_id=current_user).select_related()
    # offer_list = Design.objects.prefetch_related('offer_set').get(user_id=current_user)
    # offer_list = offer_list2.offer_set.all()
    # offer_list = Design.objects.filter(offer_id__user_id=current_user)
    print(offer_list)
    for truc in offer_list:
        print(truc)
    template = loader.get_template('community/my_offers.html')
    context = {'offer_list':offer_list}
    return HttpResponse(template.render(context, request))

def email_user(request, id):
    """Display the main web page."""
    if request.method == 'POST':
        current_user = request.user.id

        form = MessageForm(request.POST)

        if form.is_valid():
            message_title = form.cleaned_data['title']
            message_content = form.cleaned_data['content']

            receiver_ref = id

            user = User.objects.get(id=request.user.id)
            data_to_save = Message(recipent=receiver_ref, title=message_title, content=message_content, user_id=user)
            data_to_save.save()

            return redirect('messages')
    else:
        form = MessageForm()

    return render(request, 'community/email_to_user.html', {'form':form})

def make_offer(request, id):
    """Display the main web page."""

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
            print(design_ref)
            print(current_user)

            user = User.objects.get(id=request.user.id)
            design_ref_id = Design.objects.get(id=design_ref)
            data_to_save = Offer(user_id=user, design_id=design_ref_id, offer_title=offer_title, price=offer_price, carriage_price=offer_carriage_price, deadline=offer_deadline, shipment=offer_shipment)
            data_to_save.save()


# ('offer_title', 'price', 'carriage_price', 'deadline', 'shipment')


            return redirect('my_offers')
    else:
        form = OfferForm()

    return render(request, 'community/make_offer.html', {'form':form})

def offers_on_design(request, id):
    """Display the main web page."""
    current_design = id
    # current_user = request.user.id
    offer_list = Offer.objects.filter(design_id=id)
    template = loader.get_template('community/design_offer.html')
    context = {"offer_list": offer_list}
    return HttpResponse(template.render(context, request))

    # template = loader.get_template('community/make_offer.html')
    # context = {}
    # return HttpResponse(template.render(context, request))
