from rest_framework import viewsets
from rest_framework.exceptions import MethodNotAllowed
from .models import Person
from .serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()
    
    def filter_queryset(self, queryset):
        if self.request.query_params:
            raise MethodNotAllowed(method=self.request.method)
        return queryset