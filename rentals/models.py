from django.db import models

# Create your models here.
class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    class Meta:
        db_table = 'Branch'


class VehicleType(models.Model):
    vehicle_type_id = models.AutoField(primary_key=True)

    type_name = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = 'VehicleType'


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=120, unique=True)

    drivers_license_number = models.CharField(max_length=40, unique=True)
    drivers_license_expiry_date = models.DateField()

    class Meta:
        db_table = 'Customer'


class MaintenanceStaff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, db_column='branch_id')

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    office_number = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=120)

    class Meta:
        db_table = 'MaintenanceStaff'


class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)

    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE, db_column='vehicle_type_id')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, db_column='branch_id')
    license_plate = models.CharField(max_length=15, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=30, null=True, blank=True)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    current_mileage = models.IntegerField()

    class Meta:
        db_table = 'Vehicle'


class RentalAgreement(models.Model):
    class Status(models.TextChoices):
        BOOKED = 'Booked'
        ACTIVE = 'Active'
        COMPLETED = 'Completed'
        CANCELLED = 'Cancelled'

    rental_agreement_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='customer_id')
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, db_column='vehicle_id')
    pickup_branch = models.ForeignKey(Branch, on_delete=models.CASCADE, db_column='pickup_branch_id', related_name='pickup_agreements')
    return_branch = models.ForeignKey(Branch, on_delete=models.CASCADE, db_column='return_branch_id', related_name='return_agreements')
    scheduled_pickup_datetime = models.DateTimeField()
    scheduled_return_datetime = models.DateTimeField()
    actual_pickup_datetime = models.DateTimeField()
    actual_return_datetime = models.DateTimeField()
    estimated_cost = models.DecimalField(max_digits=10, decimal_places=2)
    actual_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.BOOKED)

    class Meta:
        db_table = 'RentalAgreement'


class VehicleMaintenanceRecord(models.Model):
    class IssueType(models.TextChoices):
        ROUTINE = 'Routine'
        URGENT = 'Urgent'

    class Status(models.TextChoices):
        REPORTED = 'Reported'
        IN_PROGRESS = 'InProgress'
        COMPLETE = 'Complete'
        AWAITING_PARTS = 'AwaitingParts'

    vehicle_maintenance_record_id = models.AutoField(primary_key=True)
    reported_datetime = models.DateTimeField()
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, db_column='vehicle_id')
    reporting_customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, db_column='reporting_customer_id')
    assigned_staff = models.ForeignKey(MaintenanceStaff, on_delete=models.SET_NULL, null=True, blank=True, db_column='assigned_staff_id')
    issue_type = models.CharField(max_length=10, choices=IssueType.choices)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.REPORTED)
    resolved_datetime = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'VehicleMaintenanceRecord'
