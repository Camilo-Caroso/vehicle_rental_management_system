from rest_framework import viewsets
from .models import Branch, VehicleType, Customer, MaintenanceStaff, Vehicle, RentalAgreement, VehicleMaintenanceRecord
from .serializers import BranchSerializer, VehicleTypeSerializer, CustomerSerializer, MaintenanceStaffSerializer, VehicleSerializer, RentalAgreementSerializer, VehicleMaintenanceRecordSerializer

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class MaintenanceStaffViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceStaff.objects.all()
    serializer_class = MaintenanceStaffSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class RentalAgreementViewSet(viewsets.ModelViewSet):
    queryset = RentalAgreement.objects.all()
    serializer_class = RentalAgreementSerializer

class VehicleMaintenanceRecordViewSet(viewsets.ModelViewSet):
    queryset = VehicleMaintenanceRecord.objects.all()
    serializer_class = VehicleMaintenanceRecordSerializer
