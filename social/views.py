from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserFollows
from authentication.models import User


@login_required
def subscription_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            user_to_follow = User.objects.get(username=username)
            if user_to_follow == request.user:
                messages.error(request, "Vous ne pouvez pas vous suivre vous-même.")
            # Check if the user is already following the user_to_follow
            elif UserFollows.objects.filter(user=request.user, followed_user=user_to_follow).exists():
                messages.error(request, f"Vous suivez déjà {username}")
            else:
                UserFollows.objects.get_or_create(
                    user=request.user,
                    followed_user=user_to_follow
                )
                messages.success(request, f"Vous suivez maintenant {username}")
        except User.DoesNotExist:
            messages.error(request, f"L'utilisateur {username} n'existe pas.")
        return redirect('social:subscription_page')

    # Get lists of followers and following
    following = UserFollows.objects.filter(user=request.user)
    followers = UserFollows.objects.filter(followed_user=request.user)

    return render(request, 'social/subscription.html', {
        'following': following,
        'followers': followers,
    })


@login_required
def unfollow_user(request, user_id):
    if request.method == 'POST':
        try:
            user_to_unfollow = User.objects.get(id=user_id)
            UserFollows.objects.filter(
                user=request.user,
                followed_user=user_to_unfollow
            ).delete()
            messages.success(request, f"Vous ne suivez plus {user_to_unfollow.username}")
        except User.DoesNotExist:
            messages.error(request, "Une erreur s'est produite.")
    return redirect('social:subscription_page')
