from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    links = [
        {
            "name": "UIC Main page",
            "link": "www.google.edu",
        },
        {
            "name": "UIC page 2",
            "link": "www.uic2.edu"
        },
        {
            "name": "UIC page 3",
            "link": "www.uic3.edu"
            } 
       ]
    context = {
        'links' : links 
    }
    return render(request, "webcrawler/home.html", context)

def contact(request):

    return render(request, "webcrawler/contact.html")