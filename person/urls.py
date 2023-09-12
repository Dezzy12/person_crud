from django.urls import path, include
from .views import PersonViewSet

app_name = 'person'

create_person = PersonViewSet.as_view({
    'post' : 'create'
})

person_detail = PersonViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('api/', create_person, name='person-list'),
    path('api/<int:pk>/', person_detail, name='person-detail'),
]