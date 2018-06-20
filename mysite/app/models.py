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

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        return super(Portfolio, self).save(*args, **kwargs)

class Investment(models.Model):
    portfolio = models.ForeignKey(Portfolio, editable=False, on_delete=models.PROTECT)
    owner = models.ForeignKey(User, editable=False, on_delete=models.PROTECT)
    original_amt = models.DecimalField(max_digits=10, decimal_places=2)
    btc_amt = models.DecimalField(max_digits=11, decimal_places=6)
    eth_amt = models.DecimalField(max_digits=11, decimal_places=6)
    xrp_amt = models.DecimalField(max_digits=11, decimal_places=6)
    xlm_amt = models.DecimalField(max_digits=11, decimal_places=6)
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.portfolio.portfolio_name + " " + str(self.btc_amt) + " " + str(self.eth_amt) + " " + str(self.xrp_amt) + " " + str(self.xlm_amt)

class EmbeddedTweet(models.Model):
    portfolio = models.ForeignKey(Portfolio, editable=False, on_delete=models.PROTECT)
    owner = models.ForeignKey(User, editable=False, on_delete=models.PROTECT)
    url = models.CharField(max_length=250)
    embed_code = models.CharField(max_length=20000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)