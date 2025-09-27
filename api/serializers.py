from rest_framework import serializers
from .models import Train, Station

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['name', 'code']

class TrainSerializer(serializers.ModelSerializer):
    # This will show the station's name instead of just its ID number
    current_station = StationSerializer()

    class Meta:
        model = Train
        fields = ['id', 'name', 'train_number', 'train_type', 'current_station']