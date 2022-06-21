from rest_framework.routers import DefaultRouter
from todo.api.views import TodoViewSet

# Create a router and register TodoViewSet with it.
router = DefaultRouter()
router.register(r'todo', TodoViewSet, basename='todo')

# app_name will help us do a reverse look-up latter.
app_name = 'todo'
urlpatterns = router.urls