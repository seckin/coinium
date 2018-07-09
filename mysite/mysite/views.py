from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect

def home_view(request):
    if request.user.is_authenticated:
        return redirect("/app/portfolio/1")
    return render(request, 'mysite/invest.html', {})

def invest_view(request):
    if request.user.is_authenticated:
        return redirect("/app/portfolio/1")
    return render(request, 'mysite/home.html', {})

def disclaimer_view(request):
    return render(request, 'mysite/disclaimer.html', {})

def tos_view(request):
    return render(request, 'mysite/tos.html', {})

def privacy_view(request):
    return render(request, 'mysite/privacy.html', {})
