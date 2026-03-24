from django.db import models
from users.models import User


class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('running', 'Running'),
        ('walking', 'Walking'),
        ('cycling', 'Cycling'),
        ('strength', 'Strength Training'),
        ('yoga', 'Yoga'),
        ('swimming', 'Swimming'),
        ('basketball', 'Basketball'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    distance = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, help_text="Distance in kilometers")
    calories_burned = models.PositiveIntegerField(blank=True, null=True)
    points_earned = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True)
    date_logged = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'
        ordering = ['-date_logged']

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} ({self.duration} min)"

    def save(self, *args, **kwargs):
        # Calculate points and calories if not provided
        if not self.points_earned:
            self.points_earned = self.calculate_points()
        if not self.calories_burned:
            self.calories_burned = self.calculate_calories()
        super().save(*args, **kwargs)

        # Update user's total points
        self.update_user_points()

    def calculate_points(self):
        """Calculate points based on activity type, duration, distance, and user level"""
        base_points = {
            'running': 2,
            'walking': 1,
            'cycling': 1.5,
            'strength': 3,
            'yoga': 1.5,
            'swimming': 2.5,
            'basketball': 2,
            'other': 1,
        }

        points = base_points.get(self.activity_type, 1) * self.duration

        # Bonus for distance-based activities
        if self.distance and self.activity_type in ['running', 'walking', 'cycling', 'swimming']:
            points += float(self.distance) * 0.5

        # Level multiplier
        level_multiplier = {
            'beginner': 1.0,
            'intermediate': 1.2,
            'advanced': 1.5
        }
        points *= level_multiplier.get(self.user.fitness_level, 1.0)

        return round(points)

    def calculate_calories(self):
        """Estimate calories burned based on activity type and duration"""
        # Simplified calorie calculation (MET * weight * hours)
        # Using average weight of 70kg for estimation
        met_values = {
            'running': 8.3,
            'walking': 3.8,
            'cycling': 6.8,
            'strength': 3.0,
            'yoga': 2.5,
            'swimming': 7.0,
            'basketball': 8.0,
            'other': 3.0,
        }

        met = met_values.get(self.activity_type, 3.0)
        # Calories = MET * weight(kg) * time(hours)
        calories = met * 70 * (self.duration / 60)

        return round(calories)

    def update_user_points(self):
        """Update the user's total points"""
        total_points = Activity.objects.filter(user=self.user).aggregate(
            total=models.Sum('points_earned')
        )['total'] or 0
        self.user.total_points = total_points
        self.user.save(update_fields=['total_points'])
