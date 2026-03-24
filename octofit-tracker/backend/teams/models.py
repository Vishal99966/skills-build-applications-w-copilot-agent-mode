from django.db import models
from users.models import User


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    captain = models.ForeignKey(User, on_delete=models.CASCADE, related_name='captained_teams')
    members = models.ManyToManyField(User, related_name='teams', blank=True)
    team_points = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'teams'
        ordering = ['-team_points', 'name']

    def __str__(self):
        return f"{self.name} (Captain: {self.captain.username})"

    def get_member_count(self):
        return self.members.count()

    def update_team_points(self):
        """Update team points based on member activities"""
        from activities.models import Activity
        from django.db.models import Sum

        total_points = Activity.objects.filter(
            user__in=self.members.all(),
            date_logged__gte=self.created_at
        ).aggregate(total=Sum('points_earned'))['total'] or 0

        self.team_points = total_points
        self.save(update_fields=['team_points'])

    def add_member(self, user):
        """Add a member to the team"""
        if user not in self.members.all():
            self.members.add(user)
            self.update_team_points()

    def remove_member(self, user):
        """Remove a member from the team"""
        if user in self.members.all():
            self.members.remove(user)
            self.update_team_points()


class TeamJoinRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='join_requests')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='team_join_requests')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    requested_at = models.DateTimeField(auto_now_add=True)
    responded_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'team_join_requests'
        unique_together = ['team', 'user']

    def __str__(self):
        return f"{self.user.username} -> {self.team.name} ({self.status})"
