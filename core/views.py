from django.shortcuts import render , redirect
from django.urls import reverse
from portfolio.models import Project
from contact.models import Contact
from contact.forms import ContactForm


# Create your views here.

def home(request):
    projects = Project.objects.all()
    
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            subject = request.POST.get('subject','')
            content = request.POST.get('content','')
            new_contact = Contact(name=name,email=email,subject=subject,content=content)

            new_contact.save()

            return redirect(reverse('home'))

    return render(request,'core/base.html',{'projects': projects,'form':contact_form})