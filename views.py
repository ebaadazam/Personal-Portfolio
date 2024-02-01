from django.shortcuts import render, HttpResponse
# HttpResponse added manually

# Imported Manually
from datetime import datetime
from WebApp.models import Contact
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def resume(request):
    return render(request, 'resume.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        enquiry = request.POST.get('enquiry')
        contact = Contact(name=name, email=email, number=number, enquiry=enquiry, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message is sent to Ebaad Azam')
    return render(request, 'contact.html')