import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Portfolio(models.Model):
    portfolio_name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, editable=False, on_delete=models.PROTECT)
    btc_pct = models.DecimalField(max_digits=5, decimal_places=2)
    eth_pct = models.DecimalField(max_digits=5, decimal_places=2)
    xrp_pct = models.DecimalField(max_digits=5, decimal_places=2)
    xlm_pct = models.DecimalField(max_digits=5, decimal_places=2)
    created_date = models.DateTimeField('date created')
    def __str__(self):
        return self.portfolio_name
