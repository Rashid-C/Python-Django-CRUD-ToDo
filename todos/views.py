from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = Todo.objects.filter(owner=self.request.user)
        
       
        status = self.request.query_params.get('status')
        
        if status == 'completed':
            queryset = queryset.filter(is_completed=True)
        elif status == 'pending':
            queryset = queryset.filter(is_completed=False)
            
        return queryset
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
# Create your views here.
