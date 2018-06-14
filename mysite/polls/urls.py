from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('portfolio/<int:pk>/', views.portfolio, name='portfolio'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('newportfolio/', views.newportfolio, name='newportfolio'),
    path('portfolio_perf.json', views.portfolio_perf, name='portfolio_perf'),
    path('profile/<int:user_id>', views.profile, name='profile'),
]