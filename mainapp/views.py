from rest_framework import viewsets

from mainapp.models import (
    Category, FoundItem, LostItem
)
from mainapp.serializers import (
    CategorySerializer, FoundItemSerializer, LostItemSerializer
)
from mainapp.filters import (
    CategoryFilter, FoundItemFilter, LostItemFilter
)

from django_filters.rest_framework import DjangoFilterBackend


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter


class FoundItemViewSet(viewsets.ModelViewSet):
    queryset = FoundItem.objects.all()
    serializer_class = FoundItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FoundItemFilter


class LostItemViewSet(viewsets.ModelViewSet):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LostItemFilter
