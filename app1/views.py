from django.shortcuts import render
from app1 import views


def home(request):
    return render(request, 'app1/home.html')

def about(request):
    return render(request, 'app1/about.html')


from django.template.loader import get_template
from django.http import HttpResponse

def debug_template(request):
    try:
        get_template('base.html')
        return HttpResponse("base.html found!")
    except Exception as e:
        return HttpResponse(f"Template error: {e}")