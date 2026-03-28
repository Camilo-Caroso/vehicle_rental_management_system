from rest_framework import serializers
from .models import Branch, VehicleType, Customer, MaintenanceStaff, Vehicle, RentalAgreement, VehicleMaintenanceRecord

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

class MaintenanceStaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceStaff
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class RentalAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalAgreement
        fields = '__all__'

class VehicleMaintenanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleMaintenanceRecord
        fields = '__all__'

