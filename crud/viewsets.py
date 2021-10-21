from rest_framework import viewsets
from . import models
from . import serializers

class Employeeviewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.Employeeserializer
    