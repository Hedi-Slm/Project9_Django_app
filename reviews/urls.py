from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('feed/', views.feed, name='feed'),
    path('posts/', views.posts, name='posts'),

    # Ticket URLs
    path('ticket/create/', views.ticket_create, name='ticket_create'),
    path('ticket/<int:ticket_id>/update/', views.ticket_update, name='ticket_update'),
    path('ticket/<int:ticket_id>/delete/', views.ticket_delete, name='ticket_delete'),

    # Review URLs
    path('review/<int:ticket_id>/create/', views.review_create, name='review_create'),
    path('review/<int:review_id>/update/', views.review_update, name='review_update'),
    path('review/<int:review_id>/delete/', views.review_delete, name='review_delete'),

    # Combined Ticket+Review URL
    path('create-ticket-review/', views.create_ticket_review, name='create_ticket_review'),
]
