# Generated by Django 3.1.3 on 2020-12-21 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='design',
            name='photo',
            field=models.FileField(default='default', upload_to='design_image'),
            preserve_default=False,
        ),
    ]