# Generated by Django 4.2.5 on 2023-09-18 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(upload_to='prof_pic/'),
        ),
    ]