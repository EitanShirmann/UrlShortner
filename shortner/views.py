from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid 
from .models import Url 

# Create your views here.


def index(request):
    return render(request, "index.html")
    # return HttpResponse("this works")


def create(request):
    if request.method == "POST":
        link = request.POST["link"]
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    print(url_details.link)
    return redirect("https://"+url_details.link)