from django.db import models
from users.models import User


class Achievement(models.Model):
    ACHIEVEMENT_TYPES = [
        ('first_workout', 'First Workout'),
        ('streak_7_days', '7-Day Streak'),
        ('streak_14_days', '14-Day Streak'),
        ('streak_30_days', '30-Day Streak'),
        ('points_100', '100 Points Earned'),
        ('points_500', '500 Points Earned'),
        ('points_1000', '1000 Points Earned'),
        ('team_join', 'First Team Join'),
        ('team_victory', 'Team Victory'),
        ('distance_10k', '10K Distance'),
        ('distance_50k', '50K Distance'),
        ('activities_50', '50 Activities'),
        ('activities_100', '100 Activities'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    achievement_type = models.CharField(max_length=50, choices=ACHIEVEMENT_TYPES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    points_awarded = models.PositiveIntegerField(default=0)
    badge_image = models.URLField(blank=True, null=True)
    unlocked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'achievements'
        unique_together = ['user', 'achievement_type']
        ordering = ['-unlocked_at']

    def __str__(self):
        return f"{self.user.username} - {self.title}"


class UserStreak(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='streak')
    current_streak = models.PositiveIntegerField(default=0)
    longest_streak = models.PositiveIntegerField(default=0)
    last_activity_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'user_streaks'

    def __str__(self):
        return f"{self.user.username} - Current: {self.current_streak}, Best: {self.longest_streak}"
