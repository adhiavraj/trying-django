from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World, We are learning Django Python Framework!")
    return render(request, 'website/index.html')


def about(request):
    # return HttpResponse("About Page!")
    return render(request, 'website/about.html')


def help(request):
    # return HttpResponse("Help Page!")
    return render(request, 'website/help.html')

