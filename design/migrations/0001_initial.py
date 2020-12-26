# Generated by Django 3.1.3 on 2020-12-19 22:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('plan_2d', models.CharField(max_length=50)),
                ('assembly_instruction', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('jouets', 'Jouets'), ('mobilier', 'Mobilier')], max_length=20)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_title', models.CharField(max_length=50)),
                ('date_offer', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField(null=True)),
                ('carriage_price', models.FloatField(null=True)),
                ('deadline', models.IntegerField()),
                ('shipment', models.CharField(choices=[('R', 'REGIONAL'), ('N', 'NATIONAL'), ('I', 'INTERNATIONAL')], max_length=2)),
                ('design_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='design.design')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField()),
                ('offer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='design.offer')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipent', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
                ('sended_date', models.DateTimeField(auto_now_add=True)),
                ('opened', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AddUserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
