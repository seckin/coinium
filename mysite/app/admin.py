from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Choice, Question, Portfolio, Investment
from accounts.models import Investor

# class UserInline(admin.TabularInline):
#     model = User
#     extra = 1

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

# class InvestmentInline(admin.TabularInline):
#     model = Investment
#     extra = 1

class PortfolioAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super().save_model(request, obj, form, change)
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    # list_filter = ['pub_date']
    # inlines = [InvestmentInline]
    list_display = ('portfolio_name', 'owner', 'btc_pct', 'eth_pct', 'xrp_pct', 'xlm_pct', "created_date")
    search_fields = ['portfolio_name']

class InvestmentAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.portfolio = Portfolio.objects.get(pk=10)
        super().save_model(request, obj, form, change)
    def get_portfolio(self, obj):
        return obj.portfolio
    get_portfolio.short_description = 'Portfolio'
    get_portfolio.admin_order_field = 'portfolio__id'
    # inlines = [PortfolioInline]
    list_display = ('owner', 'get_portfolio', 'original_amt', 'btc_amt', 'eth_amt', 'xrp_amt', 'xlm_amt', 'is_active', "created_at", "updated_at")

# Define an inline admin descriptor for Investor model
# which acts a bit like a singleton
class InvestorInline(admin.StackedInline):
    model = Investor
    can_delete = False
    verbose_name_plural = 'investor'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (InvestorInline, )
    def usd_amt(self, obj):
        return obj.investor.usd_amt
    list_display = ('username', 'usd_amt', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Investment, InvestmentAdmin)