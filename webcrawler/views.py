from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    
    # Get info from file

    links = ["www.google.edu", "www.facebook.com", "www.instagram.com"]

    context = {
        'links' : links
    }
    return render(request, "webcrawler/home.html", context)

def contact(request):

    return render(request, "webcrawler/contact.html")