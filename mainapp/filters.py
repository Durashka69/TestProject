from django_filters import rest_framework as filters

from mainapp.models import FoundItem, LostItem, Category


class CategoryFilter(filters.FilterSet):
    class Meta:
        model = Category
        fields = ('title',)


class FoundItemFilter(filters.FilterSet):
    class Meta:
        model = FoundItem
        fields = ('title','category',)


class LostItemFilter(filters.FilterSet):
    class Meta:
        model = LostItem
        fields = ('title','category',)
