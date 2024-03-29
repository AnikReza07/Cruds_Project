# Generated by Django 4.2.5 on 2023-09-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='prof-pic/')),
                ('email', models.EmailField(max_length=25)),
                ('phone_number', models.TextField(max_length=15)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Male', max_length=8)),
                ('address', models.TextField(max_length=40)),
                ('religion', models.CharField(choices=[('Islam', 'Islam'), ('Hindu', 'Hindu'), ('Buddha', 'Buddha'), ('Cristian', 'Cristian'), ('Others', 'Others')], default='Muslim', max_length=8)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('AB+', 'AB+'), ('O+', 'O+'), ('O-', 'O-')], default='O+', max_length=8)),
                ('date_of_birth', models.DateField()),
            ],
        ),
    ]
