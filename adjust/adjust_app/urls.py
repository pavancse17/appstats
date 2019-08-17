from django.urls import path
from . import views

urlpatterns = [
    path('', views.AppStatsListView.as_view(), name="app_stats"),
]
