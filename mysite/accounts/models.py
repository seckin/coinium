from django.db import models
from django.contrib.auth.models import User


class Investor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usd_amt = models.DecimalField(max_digits=10, decimal_places=2)

class Document(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    document_filename = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)