from .views import LoadViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'load',LoadViewSet, basename='load')
urlpatterns = router.urls