from django.contrib.auth.models import AbstractUser
from django.db import models
from bson import ObjectId


class User(AbstractUser):
    FITNESS_LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    GRADE_CHOICES = [
        ('9', '9th Grade'),
        ('10', '10th Grade'),
        ('11', '11th Grade'),
        ('12', '12th Grade'),
    ]

    # Additional fields for OctoFit Tracker
    grade_level = models.CharField(max_length=10, choices=GRADE_CHOICES, blank=True)
    fitness_level = models.CharField(max_length=20, choices=FITNESS_LEVEL_CHOICES, default='beginner')
    total_points = models.IntegerField(default=0)
    profile_picture = models.URLField(blank=True, null=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.username
