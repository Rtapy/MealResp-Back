from django.urls import path
from .views import (
    MealsListView,
    MealsDetailView,
)

urlpatterns = [
    path('meals/', MealsListView.as_view(), name='meals-list'),
    path('meals/<int:pk>/', MealsDetailView.as_view(), name='meals-detail'),
]