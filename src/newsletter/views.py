from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm, SignUpForm
from .models import SignUp
# Create your views here.
def home(request):
    title = 'Subscribe'
    form = SignUpForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }
    
    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        instance.save()
        context = {
            "title": "Thank you"
        }
        
    # if request.user.is_authenticated() and request.user.is_staff:
    #     queryset = SignUp.objects.all()
    #     context = {
    #         "queryset": queryset
    #     }
    return render(request, "home.html", context)

def contact(request):
    title = 'Contact Me'
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        # print email, message, full_name
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]
        contact_message = "%s: %s via %s"%(
            form_full_name,
            form_message,
            form_email)
        
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False)
        
    context = {
        "form": form,
        "title": title,
    }
    return render(request, "forms.html", context)
