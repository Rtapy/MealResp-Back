from django.shortcuts import render , get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView
from Meals.models import Meal, author
from .serializer import MealSerilizer, authorSerializer

class MealsListView(ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerilizer

    # lookup_field = 'slug'

    def get_queryset(self):
        return super().get_queryset()
    

class MealsDetailView(RetrieveAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerilizer
    lookup_field = 'slug'
