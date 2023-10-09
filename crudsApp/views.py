from tokenize import Name

from django.shortcuts import render, redirect
from .models import *
import os
from django.contrib import messages
# Create your views here.

def index(request):
    prof = Profile.objects.all()
    if request.method == "GET":
        search = request.GET.get('src')
        if search:
            prof = Profile.objects.filter(name__icontains = search)
        elif search == 'None':
            return redirect('home')
    else:
        prof = Profile.objects.all()

    return render(request, 'index.html', locals())


def delete(request, id):
    prof = Profile.objects.get(id=id)
    if prof.image != 'def.png':
        os.remove(prof.image.path)
    prof.delete()
    messages.warning(request, "Account Deleted.")
    return redirect('index')


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        image = request.FILES.get('image')
        number = request.POST.get('number')
        address = request.POST.get('address')
        birth = request.POST.get('birth')
        gender = request.POST.get('gender')
        religion = request.POST.get('religion')
        blood_group = request.POST.get('blood_group')
        if Profile.objects.filter(name=name).exists():
            messages.warning(request, "Another account already exixt with this name.")
            return redirect('create')
        if Profile.objects.filter(email=email).exists():
            messages.warning(request, "Another account already exixt with this email.")
            return redirect('create')
        else:
            if image:
                prof = Profile.objects.create(name = name, email = email,  phone_number = number, gender = gender, address = address, religion = religion, blood_group = blood_group, date_of_birth = birth)
                prof.save()
                messages.success(request, "Account created.")
                return redirect('index')
            else:
                prof = Profile.objects.create(name = name, email = email, phone_number = number, gender = gender, address = address, religion = religion, blood_group = blood_group, date_of_birth = birth)
                prof.save()
                messages.success(request, "Account created.")
                return redirect('index')

    return render(request, 'create.html')

def login_page(request):
    return render(request, 'login.html')

def single_prof(request, id):
    prof = Profile.objects.get(id=id)
    return render (request , 'profile_details.html', locals())


def update_prof(request, id):
    prof = Profile.objects.get(id=id)

    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        email = request.POST.get('email')
        number = request.POST.get('number')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        religion = request.POST.grt('religion')
        blood_group = request.POST.grt('blood_group')
        birth = request.POST.get('birth')
        if name:
            if image != 'def.png':
                os.remove(prof.image.path)
                prof.image = image
            prof.name = name
            prof.email = email
            prof.gender = gender
            prof.phone_number = number
            prof.address = address
            prof.religion = religion
            prof.blood_group = blood_group
            prof.date_of_birth = birth
            prof.save()
            messages.success(request, "Profile updated!")
            return redirect('index')
        else:
            messages.success(request, "Got an error")

    return render(request, 'update_profile.html', locals() ) #{'prof' : prof }