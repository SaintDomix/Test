from django.shortcuts import render, redirect

# Create your views here.


def home(request):
    return render(request, "app/home.html")


def profile(request):
    return render(request, "app/profile.html")


def eye(request):
    return render(request, "app/eye.html")


def about(request):
    return render(request, "app/about.html")


def faq(request):
    return render(request, "app/faq.html")


def lips(request):
    return render(request, "app/lips.html")


