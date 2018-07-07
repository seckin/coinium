from django.urls import path

from . import views

app_name = 'app'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('portfolio/<int:pk>/', views.portfolio, name='portfolio'),
    path('newportfolio/', views.newportfolio, name='newportfolio'),
    path('portfolio_perf/<int:portfolio_id>/', views.portfolio_perf, name='portfolio_perf'),
    path('profile/<int:user_id>', views.profile, name='profile'),
    path('create_investment/<int:portfolio_id>/', views.create_investment, name='create_investment'),
    path('tweetembed/<int:portfolio_id>/', views.embed_tweet, name='embed_tweet'),
    path('simple_upload/', views.simple_upload, name='simple_upload'),
    path('review', views.review, name='review'),
    path('fetch_prices/', views.fetch_prices, name='fetch_prices'),
    path('coins/', views.coins, name='coins'),
    path('discord/', views.mass_discord_email, name='mass_discord_email'),
    path('feed_test/', views.feed_test, name='feed_test'),
    path('follow/', views.follow, name='follow'),
    path('unfollow/', views.unfollow, name='unfollow'),
        #/<float:btc_amt>/<float:eth_amt>/<float:xrp_amt>/<float:xlm_amt>', views.create_investment, name='create_investment'),
]
