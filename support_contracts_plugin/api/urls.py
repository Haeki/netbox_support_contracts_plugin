from rest_framework import routers

from .views import SupportContractViewSet


router = routers.DefaultRouter()
router.register('contracts', SupportContractViewSet)

urlpatterns = router.urls

