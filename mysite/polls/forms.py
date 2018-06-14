from django.forms import ModelForm

from .models import Portfolio

class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['portfolio_name','btc_pct','eth_pct','xrp_pct','xlm_pct']