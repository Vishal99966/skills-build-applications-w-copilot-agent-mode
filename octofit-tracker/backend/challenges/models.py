from django.db import models
from users.models import User
from teams.models import Team


class Challenge(models.Model):
    CHALLENGE_TYPES = [
        ('individual', 'Individual'),
        ('team', 'Team'),
    ]

    METRIC_TYPES = [
        ('total_points', 'Total Points'),
        ('total_distance', 'Total Distance'),
        ('total_activities', 'Total Activities'),
        ('total_duration', 'Total Duration'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    challenge_type = models.CharField(max_length=20, choices=CHALLENGE_TYPES)
    metric_type = models.CharField(max_length=20, choices=METRIC_TYPES)
    target_value = models.PositiveIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_challenges')
    participants = models.ManyToManyField(User, related_name='challenges', blank=True)
    team_participants = models.ManyToManyField(Team, related_name='challenges', blank=True)
    winners = models.ManyToManyField(User, related_name='won_challenges', blank=True)
    winning_teams = models.ManyToManyField(Team, related_name='won_challenges', blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'challenges'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} ({self.challenge_type})"

    def is_expired(self):
        from django.utils import timezone
        return timezone.now() > self.end_date

    def get_participant_count(self):
        if self.challenge_type == 'individual':
            return self.participants.count()
        else:
            return self.team_participants.count()

    def determine_winners(self):
        """Determine winners based on challenge criteria"""
        if self.challenge_type == 'individual':
            self._determine_individual_winners()
        else:
            self._determine_team_winners()
        self.is_active = False
        self.save()

    def _determine_individual_winners(self):
        """Determine individual challenge winners"""
        from activities.models import Activity
        from django.db.models import Sum, Count

        # Get participants and their metrics
        participants_data = []
        for participant in self.participants.all():
            activities = Activity.objects.filter(
                user=participant,
                date_logged__gte=self.start_date,
                date_logged__lte=self.end_date
            )

            if self.metric_type == 'total_points':
                value = activities.aggregate(total=Sum('points_earned'))['total'] or 0
            elif self.metric_type == 'total_distance':
                value = activities.aggregate(total=Sum('distance'))['total'] or 0
            elif self.metric_type == 'total_activities':
                value = activities.count()
            elif self.metric_type == 'total_duration':
                value = activities.aggregate(total=Sum('duration'))['total'] or 0

            if value >= self.target_value:
                participants_data.append((participant, value))

        # Sort by value descending and take top winners
        participants_data.sort(key=lambda x: x[1], reverse=True)
        winners = [p[0] for p in participants_data[:3]]  # Top 3 winners

        for winner in winners:
            self.winners.add(winner)

    def _determine_team_winners(self):
        """Determine team challenge winners"""
        from activities.models import Activity
        from django.db.models import Sum

        # Get team participants and their metrics
        teams_data = []
        for team in self.team_participants.all():
            activities = Activity.objects.filter(
                user__in=team.members.all(),
                date_logged__gte=self.start_date,
                date_logged__lte=self.end_date
            )

            if self.metric_type == 'total_points':
                value = activities.aggregate(total=Sum('points_earned'))['total'] or 0
            elif self.metric_type == 'total_distance':
                value = activities.aggregate(total=Sum('distance'))['total'] or 0
            elif self.metric_type == 'total_activities':
                value = activities.count()
            elif self.metric_type == 'total_duration':
                value = activities.aggregate(total=Sum('duration'))['total'] or 0

            if value >= self.target_value:
                teams_data.append((team, value))

        # Sort by value descending and take top winning teams
        teams_data.sort(key=lambda x: x[1], reverse=True)
        winning_teams = [t[0] for t in teams_data[:3]]  # Top 3 winning teams

        for winning_team in winning_teams:
            self.winning_teams.add(winning_team)
