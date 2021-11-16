from django.urls import path, include

from rest_framework import routers

from departments.views import DepartmentsViewSet

router = routers.DefaultRouter()
router.register("", DepartmentsViewSet)

app_name = "departments"

urlpatterns = [
    path("", include(router.urls)),
]
