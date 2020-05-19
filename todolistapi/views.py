from rest_framework import  viewsets

from .serializer import DoTitleSerializer,DoListSerializer,DoCommentSerializer
from .models import DoTitle,DoList,DoComment

class DoTitleViewSet(viewsets.ModelViewSet):
    queryset = DoTitle.objects.all()
    serializer_class = DoTitleSerializer

class DoListViewSet(viewsets.ModelViewSet):
    queryset = DoList.objects.all()
    serializer_class = DoListSerializer

class DoCommentViewSet(viewsets.ModelViewSet):
    queryset = DoComment.objects.all()
    serializer_class = DoCommentSerializer