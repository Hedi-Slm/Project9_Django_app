from django.urls import path
from . import views

app_name = 'social'

urlpatterns = [
    path('subscriptions/', views.subscription_page, name='subscription_page'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
]