from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic
from django.urls import reverse

from app.models import Choice, Question

class HomeView(generic.ListView):
    model = Question
    template_name = 'mysite/home.html'