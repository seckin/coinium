from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import Investor
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            investor = Investor.objects.create(usd_amt=10000.0, user=user)
            investor.save()
            user.investor = investor
            user.save()
            mail_subject = 'Welcome to Coinium App'
            html_content = render_to_string('intro_email.html', {
                'user': user,
            })
            text_content = strip_tags(html_content)
            to_email = user.email
            email = EmailMultiAlternatives(mail_subject, text_content, 'info@coinium.app', to=[to_email], reply_to=['info@coinium.app'])
            email.attach_alternative(html_content, "text/html")
            email.send()
            request.session['just_signed_up'] = True
            # user.is_active = True
            login(request, user)
            return redirect("/app/portfolio/1")
            # return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("/app/portfolio/1")
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
