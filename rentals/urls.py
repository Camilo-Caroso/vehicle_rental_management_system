from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'branches', views.BranchViewSet)

urlpatterns = router.urls
