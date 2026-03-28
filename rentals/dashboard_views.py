from django.shortcuts import render
from .models import Branch, MaintenanceStaff, Vehicle, RentalAgreement, VehicleMaintenanceRecord, Customer, VehicleType
from django.db.models import Count
from django.views.decorators.http import require_POST

def dashboard(request):
    return render(request, 'dashboard/index.html')

def branches_partial(request):
    branches = Branch.objects.all()
    return render(request, 'dashboard/partials/branches.html', {'branches': branches})

def vehicles_partial(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'dashboard/partials/vehicles.html', {'vehicles': vehicles})

def rentals_partial(request):
    rentals = RentalAgreement.objects.filter(status='Active')
    return render(request, 'dashboard/partials/rentals.html', {'rentals': rentals})

def maintenance_partial(request):
    records = VehicleMaintenanceRecord.objects.all()
    return render(request, 'dashboard/partials/maintenance.html', {'records': records})

def customers_partial(request):
    customers = Customer.objects.all()
    return render(request, 'dashboard/partials/customers.html', {'customers': customers})

def maintenance_staff_partial(request):
    staff_list = MaintenanceStaff.objects.select_related('branch').all()
    return render(request, 'dashboard/partials/maintenance_staff.html', {'staff_list': staff_list})



def branches_list(request):
    branches = Branch.objects.annotate(
        vehicle_count=Count('vehicle', distinct=True),
        staff_count=Count('maintenancestaff', distinct=True),
        rental_count=Count('pickup_agreements', distinct=True),
    )
    return render(request, 'dashboard/branches.html', {'branches': branches})

def branch_detail(request, branch_id):
    branch = Branch.objects.get(pk=branch_id)
    vehicles = branch.vehicle_set.all()
    staff = branch.maintenancestaff_set.all()
    rentals = branch.pickup_agreements.all()
    return render(request, 'dashboard/partials/branch_detail.html', {
        'vehicles': vehicles,
        'staff': staff,
        'rentals': rentals,
    })

@require_POST
def branch_create(request):
    Branch.objects.create(
        name=request.POST['name'],
        address=request.POST['address'],
        phone=request.POST['phone'],
    )
    from django.shortcuts import redirect
    return redirect('/dashboard/branches/')







def vehicles_list(request):
    vehicles = Vehicle.objects.annotate(
        rental_count=Count('rentalagreement', distinct=True),
        maintenance_count=Count('vehiclemaintenancerecord', distinct=True),
    )
    vehicle_types = VehicleType.objects.all()
    branches = Branch.objects.all()
    return render(request, 'dashboard/vehicles.html', {
        'vehicles': vehicles,
        'vehicle_types': vehicle_types,
        'branches': branches,
    })

def vehicle_detail(request, vehicle_id):
    vehicle = Vehicle.objects.get(pk=vehicle_id)
    rentals = vehicle.rentalagreement_set.all()
    records = vehicle.vehiclemaintenancerecord_set.all()
    return render(request, 'dashboard/partials/vehicle_detail.html', {
        'rentals': rentals,
        'records': records,
    })

@require_POST
def vehicle_type_create(request):
    VehicleType.objects.create(type_name=request.POST['type_name'])
    from django.shortcuts import redirect
    return redirect('/dashboard/vehicles/')

@require_POST
def vehicle_create(request):
    Vehicle.objects.create(
        vehicle_type_id=request.POST['vehicle_type_id'],
        branch_id=request.POST['branch_id'],
        license_plate=request.POST['license_plate'],
        make=request.POST['make'],
        model=request.POST['model'],
        year=request.POST['year'],
        color=request.POST.get('color'),
        daily_rate=request.POST['daily_rate'],
        current_mileage=request.POST['current_mileage'],
    )
    from django.shortcuts import redirect
    return redirect('/dashboard/vehicles/')








def customers_list(request):
    customers = Customer.objects.annotate(
        rental_count=Count('rentalagreement', distinct=True),
        report_count=Count('vehiclemaintenancerecord', distinct=True),
    )
    return render(request, 'dashboard/customers.html', {'customers': customers})

def customer_detail(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    rentals = customer.rentalagreement_set.all()
    records = customer.vehiclemaintenancerecord_set.all()
    return render(request, 'dashboard/partials/customer_detail.html', {
        'rentals': rentals,
        'records': records,
    })

@require_POST
def customer_create(request):
    Customer.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        address=request.POST['address'],
        phone=request.POST['phone'],
        email=request.POST['email'],
        drivers_license_number=request.POST['drivers_license_number'],
        drivers_license_expiry_date=request.POST['drivers_license_expiry_date'],
    )
    from django.shortcuts import redirect
    return redirect('/dashboard/customers/')









def maintenance_staff_list(request):
    staff_list = MaintenanceStaff.objects.annotate(
        record_count=Count('vehiclemaintenancerecord', distinct=True),
    ).select_related('branch')
    branches = Branch.objects.all()
    return render(request, 'dashboard/maintenance_staff.html', {
        'staff_list': staff_list,
        'branches': branches,
    })

def maintenance_staff_detail(request, staff_id):
    staff = MaintenanceStaff.objects.get(pk=staff_id)
    records = staff.vehiclemaintenancerecord_set.all()
    return render(request, 'dashboard/partials/staff_detail.html', {'records': records})

@require_POST
def maintenance_staff_create(request):
    MaintenanceStaff.objects.create(
        branch_id=request.POST['branch_id'],
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        office_number=request.POST.get('office_number') or None,
        phone=request.POST['phone'],
        email=request.POST['email'],
    )
    from django.shortcuts import redirect
    return redirect('/dashboard/maintenance-staff/')







def rental_agreements_list(request):
    rentals = RentalAgreement.objects.select_related(
        'customer', 'vehicle', 'pickup_branch', 'return_branch'
    ).all()
    customers = Customer.objects.all()
    vehicles = Vehicle.objects.all()
    branches = Branch.objects.all()
    return render(request, 'dashboard/rental_agreements.html', {
        'rentals': rentals,
        'customers': customers,
        'vehicles': vehicles,
        'branches': branches,
    })

def rental_agreement_detail(request, rental_id):
    rental = RentalAgreement.objects.select_related('vehicle').get(pk=rental_id)
    return render(request, 'dashboard/partials/rental_detail.html', {'rental': rental})

@require_POST
def rental_agreement_create(request):
    RentalAgreement.objects.create(
        customer_id=request.POST['customer_id'],
        vehicle_id=request.POST['vehicle_id'],
        pickup_branch_id=request.POST['pickup_branch_id'],
        return_branch_id=request.POST['return_branch_id'],
        scheduled_pickup_datetime=request.POST['scheduled_pickup_datetime'],
        scheduled_return_datetime=request.POST['scheduled_return_datetime'],
        actual_pickup_datetime=request.POST['actual_pickup_datetime'],
        actual_return_datetime=request.POST['actual_return_datetime'],
        estimated_cost=request.POST['estimated_cost'],
        actual_cost=request.POST['actual_cost'],
        status=request.POST['status'],
    )
    from django.shortcuts import redirect
    return redirect('/dashboard/rental-agreements/')







def maintenance_records_list(request):
    records = VehicleMaintenanceRecord.objects.select_related(
        'vehicle', 'reporting_customer', 'assigned_staff'
    ).all()
    vehicles = Vehicle.objects.all()
    customers = Customer.objects.all()
    staff_list = MaintenanceStaff.objects.all()
    return render(request, 'dashboard/maintenance_records.html', {
        'records': records,
        'vehicles': vehicles,
        'customers': customers,
        'staff_list': staff_list,
    })

def maintenance_record_detail(request, record_id):
    record = VehicleMaintenanceRecord.objects.select_related('vehicle').get(pk=record_id)
    return render(request, 'dashboard/partials/record_detail.html', {'record': record})


@require_POST
def maintenance_record_create(request):
    VehicleMaintenanceRecord.objects.create(
        vehicle_id=request.POST['vehicle_id'],
        reporting_customer_id=request.POST.get('reporting_customer_id') or None,
        assigned_staff_id=request.POST.get('assigned_staff_id') or None,
        reported_datetime=request.POST['reported_datetime'],
        issue_type=request.POST['issue_type'],
        description=request.POST['description'],
        status=request.POST['status'],
        notes=request.POST.get('notes') or None,
        resolved_datetime=request.POST.get('resolved_datetime') or None,
    )
    from django.shortcuts import redirect
    return redirect('/dashboard/maintenance-records/')
