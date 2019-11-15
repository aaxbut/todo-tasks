from rest_framework import routers

from .views import TasksViewSet

router = routers.DefaultRouter()
router.register(
    r'tasks',
    TasksViewSet,
    base_name='tasks'
)

urlpatterns = router.urls
