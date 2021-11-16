from django.urls import path, include

from rest_framework import routers

from headquarters.views import HeadquarterViewSet

router = routers.DefaultRouter()
router.register("", HeadquarterViewSet)

app_name = "headquarters"

urlpatterns = [
    path("", include(router.urls)),
]
