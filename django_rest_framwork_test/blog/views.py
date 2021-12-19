import django_filters
from rest_framework import filters, viewsets

from .models import Entry, User
from .serializer import EntrySerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    # モデルのクエリセット
    queryset = User.objects.all()
    # シリアライザーの指定
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    # モデルのクエリセット
    queryset = Entry.objects.all()
    # シリアライザーの指定
    serializer_class = EntrySerializer
