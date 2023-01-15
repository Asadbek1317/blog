from django.http import HttpResponse
from django.shortcuts import render

from app.models import Contact, Register


# Create your views here.

def index(request):
    if request.method == "POST":
        contact=Contact()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        text = request.POST.get('text')
        contact.name=name
        contact.phone=phone
        contact.text=text
        contact.save()
        return render(request, 'register.html')

    return render(request, 'index.html')


def register(request):
    if request.method == "POST":
        register=Register()
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        register.name=name
        register.phone=phone
        register.save()
        return HttpResponse('salom')
    return render(request, 'register.html')
