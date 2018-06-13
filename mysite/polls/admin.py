from django.contrib import admin
from django.contrib.auth.models import User

from .models import Choice, Question, Portfolio

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

class PortfolioAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        super().save_model(request, obj, form, change)
    # list_display = ('question_text', 'pub_date', 'was_published_recently')
    # list_filter = ['pub_date']
    # inlines = [UserInline]
    list_display = ('portfolio_name', 'owner', 'btc_pct', 'eth_pct', 'xrp_pct', 'xlm_pct', "created_date")
    search_fields = ['portfolio_name']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Portfolio, PortfolioAdmin)