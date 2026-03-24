from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import timedelta
from .models import Activity
from .serializers import ActivitySerializer, ActivityCreateSerializer


class ActivityListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    filterset_fields = ['activity_type', 'date_logged']

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ActivityCreateSerializer
        return ActivitySerializer

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ActivityDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ActivitySerializer

    def get_queryset(self):
        return Activity.objects.filter(user=self.request.user)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def activity_stats(request):
    """Get user's activity statistics"""
    user = request.user
    activities = Activity.objects.filter(user=user)

    # Overall stats
    total_activities = activities.count()
    total_points = activities.aggregate(Sum('points_earned'))['points_earned__sum'] or 0
    total_duration = activities.aggregate(Sum('duration'))['duration__sum'] or 0
    total_distance = activities.aggregate(Sum('distance'))['distance__sum'] or 0
    total_calories = activities.aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0

    # This week's stats
    week_start = timezone.now() - timedelta(days=7)
    week_activities = activities.filter(date_logged__gte=week_start)
    week_points = week_activities.aggregate(Sum('points_earned'))['points_earned__sum'] or 0
    week_activities_count = week_activities.count()

    # Activity type breakdown
    activity_breakdown = activities.values('activity_type').annotate(
        count=Count('id'),
        total_points=Sum('points_earned'),
        total_duration=Sum('duration')
    ).order_by('-count')

    stats = {
        'overall': {
            'total_activities': total_activities,
            'total_points': total_points,
            'total_duration_minutes': total_duration,
            'total_distance_km': float(total_distance) if total_distance else 0,
            'total_calories': total_calories,
        },
        'this_week': {
            'activities_count': week_activities_count,
            'points_earned': week_points,
        },
        'activity_breakdown': list(activity_breakdown),
    }

    return Response(stats)
