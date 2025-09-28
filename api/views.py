from rest_framework import generics
from .models import Train
from .serializers import TrainSerializer

class TrainList(generics.ListAPIView):
    queryset = Train.objects.all()
    serializer_class = TrainSerializer