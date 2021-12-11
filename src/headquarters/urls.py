from django.urls import path, include

from rest_framework import routers

from headquarters.views import HeadquartersViewSet

router = routers.DefaultRouter()
router.register("", HeadquartersViewSet)

app_name = "headquarters"

urlpatterns = [
    path("", include(router.urls)),
]
