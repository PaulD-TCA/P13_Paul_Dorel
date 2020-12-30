from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Design(models.Model):
    "fields of Design table"
    CATEGORIES = (
        ('jouets', 'Jouets'),
        ('mobilier', 'Mobilier'),
    )
    design_name = models.CharField(max_length=50)
    design_image = models.FileField(upload_to='design_image')
    plan_2d = models.FileField(upload_to='design_2d_plan')
    plan_3d = models.FileField(upload_to='design_3d_plan')
    assembly_instruction = models.FileField(upload_to='design_assy_ins')
    description = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    creation_date = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.design_name

class AddUserInfo(models.Model):
    "fields of additional user information table"
    street = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.street

class Message(models.Model):
    "fields of messages table"
    recipent = models.IntegerField()
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    sended_date = models.DateTimeField(auto_now_add=True)
    opened = models.BooleanField(default=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Offer(models.Model):
    "fields of offer table"
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    design_id = models.ForeignKey(Design, on_delete=models.CASCADE)
    offer_title = models.CharField(max_length=50)
    date_offer = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(null=True)
    carriage_price = models.FloatField(null=True)
    deadline = models.IntegerField()
    SHIPMENT_AREA = (
        ('R', 'REGIONAL'),
        ('N', 'NATIONAL'),
        ('I', 'INTERNATIONAL'),
    )
    shipment = models.CharField(max_length=2, choices=SHIPMENT_AREA)


    def __str__(self):
        return self.offer_title

class Order(models.Model):
    "fields of order table"
    order_date = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    offer_id = models.ForeignKey(Offer, on_delete=models.CASCADE)

    def __str__(self):
        return self.quantity
