from rest_framework import serializers
from Meals.models import author, Meal

class MealSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'

class authorSerializer(serializers.ModelSerializer):
    class Meta:
        model = author
        fields = '__all__'
