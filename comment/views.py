from rest_framework.viewsets import ModelViewSet
from .models import Comment
from .serializers import CommentSerializer
from problem.views import PermissionMixin


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer