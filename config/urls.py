"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from rentals import dashboard_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('health/', views.health),

    path('api/', include('rentals.urls')),

    path('dashboard/', dashboard_views.dashboard),
    path('dashboard/partials/branches/', dashboard_views.branches_partial),
    path('dashboard/partials/vehicles/', dashboard_views.vehicles_partial),
    path('dashboard/partials/rentals/', dashboard_views.rentals_partial),
    path('dashboard/partials/maintenance/', dashboard_views.maintenance_partial),
    path('dashboard/partials/customers/', dashboard_views.customers_partial),
    path('dashboard/partials/maintenance-staff/', dashboard_views.maintenance_staff_partial),

    path('dashboard/branches/', dashboard_views.branches_list),
    path('dashboard/branches/create/', dashboard_views.branch_create),
    path('dashboard/branches/<int:branch_id>/detail/', dashboard_views.branch_detail),

    path('dashboard/vehicles/', dashboard_views.vehicles_list),
    path('dashboard/vehicles/<int:vehicle_id>/detail/', dashboard_views.vehicle_detail),
    path('dashboard/vehicle-types/create/', dashboard_views.vehicle_type_create),
    path('dashboard/vehicles/create/', dashboard_views.vehicle_create),

    path('dashboard/customers/', dashboard_views.customers_list),
    path('dashboard/customers/<int:customer_id>/detail/', dashboard_views.customer_detail),
    path('dashboard/customers/create/', dashboard_views.customer_create),

    path('dashboard/maintenance-staff/', dashboard_views.maintenance_staff_list),
    path('dashboard/maintenance-staff/<int:staff_id>/detail/', dashboard_views.maintenance_staff_detail),
    path('dashboard/maintenance-staff/create/', dashboard_views.maintenance_staff_create),

    path('dashboard/rental-agreements/', dashboard_views.rental_agreements_list),
    path('dashboard/rental-agreements/<int:rental_id>/detail/', dashboard_views.rental_agreement_detail),
    path('dashboard/rental-agreements/create/', dashboard_views.rental_agreement_create),

    path('dashboard/maintenance-records/', dashboard_views.maintenance_records_list),
    path('dashboard/maintenance-records/<int:record_id>/detail/', dashboard_views.maintenance_record_detail),
    path('dashboard/maintenance-records/create/', dashboard_views.maintenance_record_create),
]
