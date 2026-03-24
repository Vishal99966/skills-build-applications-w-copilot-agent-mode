from rest_framework import serializers
from .models import Activity


class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    activity_type_display = serializers.CharField(source='get_activity_type_display', read_only=True)

    class Meta:
        model = Activity
        fields = [
            'id', 'user', 'activity_type', 'activity_type_display', 'duration',
            'distance', 'calories_burned', 'points_earned', 'notes',
            'date_logged'
        ]
        read_only_fields = ['id', 'calories_burned', 'points_earned', 'date_logged']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class ActivityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['activity_type', 'duration', 'distance', 'notes']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)