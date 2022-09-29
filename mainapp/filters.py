from django_filters import rest_framework as filters

from mainapp.models import Item, Category


class CategoryFilter(filters.FilterSet):
    class Meta:
        model = Category
        fields = ('title',)


class FoundItemFilter(filters.FilterSet):
    class Meta:
        model = Item
        fields = ('title','category',)
