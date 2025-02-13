from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import CharField, Value
from django.db import transaction
from itertools import chain

from .models import Ticket, Review
from .forms import TicketForm, ReviewForm, CombinedTicketReviewForm


@login_required
def feed(request):
    # Get reviews from:  followed users / current user / reviews done on current user tickets
    reviews = (Review.objects.filter(user__in=request.user.following.values('followed_user'))
               | Review.objects.filter(user=request.user) | Review.objects.filter(ticket__user=request.user))
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))

    # Get tickets from: followed users / current user
    tickets = (Ticket.objects.filter(user__in=request.user.following.values('followed_user'))
               | Ticket.objects.filter(user=request.user))
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    # Combine and sort
    posts = sorted(chain(reviews, tickets), key=lambda post: post.time_created, reverse=True)
    return render(request, 'reviews/feed.html', {'posts': posts})


# Ticket Views
@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            messages.success(request, 'Your ticket has been created!')
            return redirect('reviews:feed')
    else:
        form = TicketForm()
    return render(request, 'reviews/ticket_create.html', {'form': form})


@login_required
def ticket_update(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your ticket has been updated!')
            return redirect('reviews:feed')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'reviews/ticket_update.html', {'form': form, 'ticket': ticket})


@login_required
def ticket_delete(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, user=request.user)
    if request.method == 'POST':
        ticket.delete()
        messages.success(request, 'Your ticket has been deleted!')
        return redirect('reviews:feed')
    return render(request, 'reviews/ticket_delete.html', {'ticket': ticket})


# Review Views
@login_required
def review_create(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    # Check if user already reviewed this ticket
    if Review.objects.filter(ticket=ticket, user=request.user).exists():
        messages.error(request, 'You have already reviewed this ticket!')
        return redirect('reviews:feed')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            messages.success(request, 'Your review has been created!')
            return redirect('reviews:feed')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_create.html', {
        'form': form,
        'ticket': ticket
    })


@login_required
def review_update(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated!')
            return redirect('reviews:feed')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'reviews/review_update.html', {
        'form': form,
        'review': review
    })


@login_required
def review_delete(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Your review has been deleted!')
        return redirect('reviews:feed')
    return render(request, 'reviews/review_delete.html', {'review': review})


# Combined Ticket and Review creation
@login_required
def create_ticket_review(request):
    if request.method == 'POST':
        form = CombinedTicketReviewForm(request.POST, request.FILES)
        if form.is_valid():
            with transaction.atomic():
                # Create ticket
                ticket = Ticket.objects.create(
                    title=form.cleaned_data['title'],
                    description=form.cleaned_data['description'],
                    image=form.cleaned_data.get('image'),
                    user=request.user
                )

                # Create review
                Review.objects.create(
                    ticket=ticket,
                    headline=form.cleaned_data['headline'],
                    rating=form.cleaned_data['rating'],
                    body=form.cleaned_data['body'],
                    user=request.user
                )

            messages.success(request, 'Your ticket and review have been created!')
            return redirect('reviews:feed')
    else:
        form = CombinedTicketReviewForm()

    # Group fields for the template
    ticket_fields = ['title', 'description', 'image']
    review_fields = ['headline', 'rating', 'body']

    grouped_fields = {
        'ticket_fields': [form[field] for field in ticket_fields],
        'review_fields': [form[field] for field in review_fields],
    }

    return render(request, 'reviews/create_ticket_review.html', {
        'form': form, 'grouped_fields': grouped_fields})
