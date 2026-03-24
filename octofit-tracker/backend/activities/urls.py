from django.urls import path
from . import views

app_name = 'activities'

urlpatterns = [
    path('', views.ActivityListCreateView.as_view(), name='activity-list-create'),
    path('<str:pk>/', views.ActivityDetailView.as_view(), name='activity-detail'),
    path('stats/', views.activity_stats, name='activity-stats'),
]