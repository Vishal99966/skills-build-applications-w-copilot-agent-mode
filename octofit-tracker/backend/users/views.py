from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserProfileSerializer

User = get_user_model()


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_stats(request):
    """Get user statistics"""
    user = request.user

    # Get activity stats
    activities = user.activities.all()
    total_activities = activities.count()
    total_points = sum(activity.points_earned for activity in activities)
    total_duration = sum(activity.duration for activity in activities)
    total_distance = sum(float(activity.distance or 0) for activity in activities)

    # Get achievement count
    achievement_count = user.achievements.count()

    # Get team info
    teams = user.teams.all()
    team_count = teams.count()

    stats = {
        'total_activities': total_activities,
        'total_points': total_points,
        'total_duration_minutes': total_duration,
        'total_distance_km': round(total_distance, 2),
        'achievement_count': achievement_count,
        'team_count': team_count,
        'current_streak': getattr(user.streak, 'current_streak', 0) if hasattr(user, 'streak') else 0,
        'longest_streak': getattr(user.streak, 'longest_streak', 0) if hasattr(user, 'streak') else 0,
    }

    return Response(stats)
