from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'branches', views.BranchViewSet)
router.register(r'vehicle-types', views.VehicleTypeViewSet)
router.register(r'customers', views.CustomerViewSet)
router.register(r'maintenance-staff', views.MaintenanceStaffViewSet)
router.register(r'vehicles', views.VehicleViewSet)
router.register(r'rental-agreements', views.RentalAgreementViewSet)
router.register(r'maintenance-records', views.VehicleMaintenanceRecordViewSet)

urlpatterns = router.urls
