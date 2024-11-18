from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
    context={}

    home_carusel = HomeCarusel.objects.all()
    context["home_carusel"] = home_carusel
    

    service_start = ServiceStart.objects.all()[:4]
    context["service_start"] = service_start
    print(service_start)

    about_start = AboutStart.objects.all()
    context["about_start"] = about_start
    print(about_start)

    testimonial = Testimonial.objects.all()
    context["testimonial"] = testimonial
    print(testimonial)

    contact_information = ContactInformation.objects.all()
    context["contact_information"] = contact_information
    print(contact_information)

    contact = Contact.objects.all()
    context["contact"] = contact
    print(contact)

    footer_icons = FooterIcons.objects.all()
    context["footer_icons"] = footer_icons
    print(footer_icons)

    return render(request, "home/index.html", context)
    


def about(request):
    return render(request, "home/about.html")


def contact(request):
    return render(request, "home/contact.html")



def cources(request):
    return render(request, "home/courses.html")


def testimonial(request):
    return render(request, "home/testimonial.html")


def team(request):
    return render(request, "home/team.html")


def error(request):
    return render(request, "home/404.html")
