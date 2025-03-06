from django.db import models
from django.db.models import UniqueConstraint, CheckConstraint
from django.conf import settings


class UserFollows(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='following', on_delete=models.CASCADE)
    followed_user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                      related_name='followed_by', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            # Prevent duplicate follows
            UniqueConstraint(fields=['user', 'followed_user'], name='unique_follow'),
            # Prevent self-follow
            CheckConstraint(check=~models.Q(user=models.F('followed_user')),
                            name='prevent_self_follow')
        ]
