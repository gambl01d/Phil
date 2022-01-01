from django.shortcuts import render


def HomeView(request):
    return  render(request, 'Home.html')

# Create your views here.
