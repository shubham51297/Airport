from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import Technician,Airplane,Employee, Test, TestRecords, Monitor
from .serializers import TechnicianSerializer,AirplaneSerializer,EmployeeSerializer, TestSerializer, TestRecordsSerializer, MonitorSerializer


class TechnicianView(APIView, UpdateModelMixin,DestroyModelMixin,):
    def get(self, request, ssn=None):
        if ssn:
            try:
                queryset = Technician.objects.raw("select 1 as id, ssn from technician where ssn = %s",[ssn])
                read_serializer = TechnicianSerializer(queryset, many=True)
                return Response(read_serializer.data)
            except Technician.DoesNotExist:
                return Response({'errors': 'This todo item does not exist.'}, status=400)
        else:
            queryset = Technician.objects.raw('SELECT 1 as id, ssn FROM Technician')
            read_serializer = TechnicianSerializer(queryset, many=True)
        return Response(read_serializer.data)

class AirplaneView(APIView, UpdateModelMixin,DestroyModelMixin,):
    def get(self, request, regnum=None):
        if regnum:
            try:
                queryset = Airplane.objects.raw("select 1 as id, regnum, modelnumber from Airplane where regnum = %s",[regnum])
                read_serializer = AirplaneSerializer(queryset, many=True)
                return Response(read_serializer.data)
            except Technician.DoesNotExist:
                return Response({'errors': 'This todo item does not exist.'}, status=400)
        else:
            queryset = Airplane.objects.raw('SELECT 1 as id, regnum , modelnumber FROM Airplane')
            read_serializer = AirplaneSerializer(queryset, many=True)
        return Response(read_serializer.data)

class EmployeeView(APIView, UpdateModelMixin,DestroyModelMixin,):
    def get(self, request, ssn=None):
        if ssn:
            try:
                queryset = Employee.objects.raw("select 1 as id, ssn, name, phone, sex, salary, street, city, country from Employee where ssn = %s",[ssn])
                read_serializer = EmployeeSerializer(queryset, many=True)
                return Response(read_serializer.data)
            except Technician.DoesNotExist:
                return Response({'errors': 'This todo item does not exist.'}, status=400)
        else:
            queryset = Employee.objects.raw('SELECT 1 as id, ssn, name, phone, sex, salary, street, city, country FROM Employee')
            read_serializer = EmployeeSerializer(queryset, many=True)
        return Response(read_serializer.data)

class TestView(APIView, UpdateModelMixin,DestroyModelMixin,):
    def get(self, request, mno=None):
        if mno:
            try:
                queryset = Test.objects.raw("select 1 as id, ffa_num, name, max_score, modelnumber from Test where modelnumber = %s",[mno])
                read_serializer = TestSerializer(queryset, many=True)
                return Response(read_serializer.data)
            except Technician.DoesNotExist:
                return Response({'errors': 'This todo item does not exist.'}, status=400)
        else:
            queryset = Test.objects.raw('SELECT 1 as id, ffa_num, name, max_score, modelnumber from Test')
            read_serializer = TestSerializer(queryset, many=True)
        return Response(read_serializer.data)

class TestRecordsView(APIView, UpdateModelMixin,DestroyModelMixin,):
    def get(self, request, regnum=None):
        if regnum:
            try:
                queryset = TestRecords.objects.raw("select 1 as id, timestmp, ssn, regnum, ffa_num, score, hour from Test_Records where regnum = %s",[regnum])
                read_serializer = TestRecordsSerializer(queryset, many=True)
                return Response(read_serializer.data)
            except Technician.DoesNotExist:
                return Response({'errors': 'This todo item does not exist.'}, status=400)
        else:
            queryset = TestRecords.objects.raw('SELECT 1 as id, timestmp, ssn, regnum, ffa_num, score, hour from Test_Records')
            read_serializer = TestRecordsSerializer(queryset, many=True)
        return Response(read_serializer.data)

class PlanTestSchView(APIView, UpdateModelMixin,DestroyModelMixin,):
    def get(self, request, ssn=None):
        if ssn:
            try:
                queryset = TestRecords.objects.raw("select 1 as id, timestmp, ssn, regnum, ffa_num, score, hour from Test_Records where ssn = %s",[ssn])
                read_serializer = TestRecordsSerializer(queryset, many=True)
                return Response(read_serializer.data)
            except Technician.DoesNotExist:
                return Response({'errors': 'This todo item does not exist.'}, status=400)

class MonitorView(APIView, UpdateModelMixin,DestroyModelMixin,):
    def get(self, request, regnum=None):
        if regnum:
            try:
                queryset = Monitor.objects.raw("select 1 as id, ssn, regnum from Monitor where regnum = %s",[regnum])
                read_serializer = MonitorSerializer(queryset, many=True)
                return Response(read_serializer.data)
            except Monitor.DoesNotExist:
                return Response({'errors': 'This todo item does not exist.'}, status=400)
        else:
            queryset = Monitor.objects.raw('SELECT 1 as id, ssn, regnum from Monitor')
            read_serializer = MonitorSerializer(queryset, many=True)
        return Response(read_serializer.data)

class MonitorATCView(APIView, UpdateModelMixin,DestroyModelMixin,):
    def get(self, request, ssn=None):
        if ssn:
            try:
                queryset = Monitor.objects.raw("select 1 as id, ssn, regnum from Monitor where ssn = %s",[ssn])
                read_serializer = MonitorSerializer(queryset, many=True)
                return Response(read_serializer.data)
            except Monitor.DoesNotExist:
                return Response({'errors': 'This todo item does not exist.'}, status=400)
        else:
            queryset = Monitor.objects.raw('SELECT 1 as id, ssn, regnum from Monitor')
            read_serializer = MonitorSerializer(queryset, many=True)
        return Response(read_serializer.data)

