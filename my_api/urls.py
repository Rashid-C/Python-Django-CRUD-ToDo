
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todos.views import TodoViewSet

router = DefaultRouter()
router.register(r'api/todos', TodoViewSet, basename='todo')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), # Connects our todo API paths
]
