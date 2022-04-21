from rest_framework import serializers

from .models import Technician, Airplane, Employee, Test,TestRecords,Monitor

class TechnicianSerializer(serializers.ModelSerializer):
  class Meta:
    model = Technician
    fields = '__all__'

class AirplaneSerializer(serializers.ModelSerializer):
  class Meta:
    model = Airplane
    fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
  class Meta:
    model = Test
    fields = '__all__'

class TestRecordsSerializer(serializers.ModelSerializer):
  class Meta:
    model = TestRecords
    fields = '__all__'

class MonitorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Monitor
    fields = '__all__'