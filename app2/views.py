from django.shortcuts import render

def info(request):
    return render(request, 'app2/info.html')
