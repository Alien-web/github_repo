# Generated by Django 3.1.7 on 2021-03-11 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='img',
            field=models.ImageField(default='image/bali.jpg', upload_to='pics'),
        ),
    ]
