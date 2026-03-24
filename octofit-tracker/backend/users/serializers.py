from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer

User = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    grade_level = serializers.ChoiceField(choices=User.GRADE_CHOICES, required=False)
    fitness_level = serializers.ChoiceField(choices=User.FITNESS_LEVEL_CHOICES, required=False)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['first_name'] = self.validated_data.get('first_name', '')
        data['last_name'] = self.validated_data.get('last_name', '')
        data['grade_level'] = self.validated_data.get('grade_level', '9')
        data['fitness_level'] = self.validated_data.get('fitness_level', 'beginner')
        return data


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 'full_name',
            'grade_level', 'fitness_level', 'total_points', 'profile_picture',
            'date_joined', 'last_login'
        ]
        read_only_fields = ['id', 'total_points', 'date_joined', 'last_login']

    def get_full_name(self, obj):
        return obj.get_full_name()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name',
            'grade_level', 'fitness_level', 'profile_picture'
        ]

    def update(self, instance, validated_data):
        # Prevent username changes
        validated_data.pop('username', None)
        return super().update(instance, validated_data)


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name', 'full_name',
            'grade_level', 'fitness_level', 'total_points', 'profile_picture',
            'date_joined', 'last_login'
        ]
        read_only_fields = ['id', 'total_points', 'date_joined', 'last_login']

    def get_full_name(self, obj):
        return obj.get_full_name()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name',
            'grade_level', 'fitness_level', 'profile_picture'
        ]

    def update(self, instance, validated_data):
        # Prevent username changes
        validated_data.pop('username', None)
        return super().update(instance, validated_data)