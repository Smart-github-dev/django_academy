from django.db import models


class Users_activity(models.Model):
    action = models.CharField(max_length=20)
    mentor_name = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(
        blank=True, null=True, help_text="HH:MM:SS DD Mmm YY, YYYY PST"
    )

    def __str__(self):
        return self.commit_id
