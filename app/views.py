from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import App
from django.conf import settings
from django.core.mail import send_mail
from .forms import ContactForm
from django.db.models import Q

# Create your views here.
def index(request):
    search_post = request.GET.get('search')
    if search_post:
        apps = App.objects.filter(Q(name__contains=search_post) | Q(providedby__contains=search_post) | Q(eligibilitycriteria__contains=search_post) |Q(exam__contains=search_post) | Q(scholarshipamount__contains=search_post) | Q(applicationfees__contains=search_post) | Q(deadline__contains=search_post) |Q(link__contains=search_post))
    else:
        apps = App.objects.all().order_by("-scholarshipamount")
    return render(request, "app/index.html",{
        "apps":apps
    })

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            return render(request, 'app/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'app/contact.html', context)

def about(request):
    return render(request, "app/about.html")

def landing(request):
    return render(request, "app/landing.html")

def category(request):
    search_post = request.GET.get('dropdown')
    search_level = request.GET.get('level')
    search_salary = request.GET.get('salary')
    if search_post:
        apps = App.objects.filter(Q(category=search_post) & Q(levels=search_level) & Q(salaries=search_salary))
    else:
        apps = App.objects.all().order_by("-name")
    return render(request, "app/filter.html",{
        "apps":apps
    })