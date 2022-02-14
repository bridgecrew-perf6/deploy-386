from rest_framework.viewsets import ModelViewSet
from .serializers import ProblemSerializer, ReplySerializer
from .models import Problem, Reply
from account.permissions import IsActive
from rest_framework.permissions import AllowAny
from .permissions import IsAuthorPermission
from rest_framework.permissions import AllowAny

class PermissionMixin:
    def get_permission(self):
        if self.action == 'create':
            permissions = [IsActive]
        elif self.action in ['update', 'partioal_update']:
            permissions = [IsAuthorPermission]
        else:
            permissions = [AllowAny]
        return [permisson() for permisson in permissions]      


class ProblemViewSet(PermissionMixin, ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['action'] = self.action
        return context
    

class ReplyViewSet(PermissionMixin, ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
