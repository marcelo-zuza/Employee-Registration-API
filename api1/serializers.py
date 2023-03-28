from rest_framework import serializers
from api1.models import Job, Employee


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = list_display = ('id', 'job', 'salary', 'created', 'modified')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'job', 'image', 'active', 'created', 'modified')
