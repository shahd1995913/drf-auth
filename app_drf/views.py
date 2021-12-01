from rest_framework import generics

from .models import Car

from .serializers import CarSerializer

from .permissions import IsOwnerOrReadOnly

class CarList(generics.ListCreateAPIView):

    queryset = Car.objects.all()

    serializer_class = CarSerializer

class CarDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Car.objects.all()

    serializer_class = CarSerializer

    permission_classes = (IsOwnerOrReadOnly,)
