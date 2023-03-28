from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from api1.models import Job, Employee
from api1.serializers import JobSerializer, EmployeeSerializer


class IndexView(TemplateView):
    template_name = 'index.html'


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        job = self.get_object()
        serializer = EmployeeSerializer(job.employees.all(), many=True)
        return Response(serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
