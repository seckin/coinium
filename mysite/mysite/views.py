from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect

def home_view(request):
    if request.user.is_authenticated:
        return redirect("/app/portfolio/1")
    return render(request, 'mysite/home.html', {})
