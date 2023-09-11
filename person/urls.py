from django.urls import path, include
from rest_framework import routers
from .views import PersonViewSet

app_name = 'person'

router = routers.DefaultRouter()
router.register(r'', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
