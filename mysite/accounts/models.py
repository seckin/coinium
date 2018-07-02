from django.db import models
from django.contrib.auth.models import User


class Investor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usd_amt = models.DecimalField(max_digits=10, decimal_places=2)
    is_approved = models.BooleanField(default=False)
    facebook = models.CharField(max_length=250, default="")
    twitter = models.CharField(max_length=250, default="")
    linkedin = models.CharField(max_length=250, default="")
    website = models.CharField(max_length=250, default="")
    location = models.CharField(max_length=250, default="")
    university = models.CharField(max_length=250, default="")
    experience = models.CharField(max_length=250, default="")

class Document(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    document_filename = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)