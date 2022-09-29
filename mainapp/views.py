from rest_framework import viewsets

from mainapp.models import (
    Category, Item
)
from mainapp.serializers import (
    CategorySerializer, ItemSerializer
)
from mainapp.filters import (
    CategoryFilter, FoundItemFilter
)

from django_filters.rest_framework import DjangoFilterBackend


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FoundItemFilter


# class LostItemViewSet(viewsets.ModelViewSet):
#     queryset = LostItem.objects.all()
#     serializer_class = LostItemSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_class = LostItemFilter
