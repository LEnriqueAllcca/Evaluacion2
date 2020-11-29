from rest_framework import generics,filters
from todos import models
from .serializers import TodoSerializer

class TodoAPIView(generics.ListCreateAPIView):
    search_fields = ['codTipo__nombreTipo']
    filter_backends = (filters.SearchFilter, )
    queryset = models.Institucion.objects.all()
    serializer_class = TodoSerializer

class RucAPIView(generics.ListCreateAPIView):
    search_fields = ['Ruc']
    filter_backends = (filters.SearchFilter, )
    queryset = models.Institucion.objects.all()
    serializer_class = TodoSerializer

class NombreAPIView(generics.ListCreateAPIView):
    search_fields = ['nombInsti']
    filter_backends = (filters.SearchFilter, )
    queryset = models.Institucion.objects.all()
    serializer_class = TodoSerializer