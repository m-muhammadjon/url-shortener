from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('short-url/', views.short_url, name='short_url'),
    path('history/', views.history, name='history'),
    path('s/<str:shorted>/', views.shorted_detail, name='shorted_detail'),
    path('', views.home, name='home'),
    path('<str:shorted>/', views.redirect_to_original_link, name='redirect_to_original_link'),
]
