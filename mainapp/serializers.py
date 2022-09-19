from rest_framework import serializers

from mainapp.models import FoundItem, LostItem, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


class FoundItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundItem
        fields = (
            'title', 'category', 'date',
            'picture',
            'geotag', 'description',
            'pickup_location'
        )
        

class LostItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostItem
        fields = (
            'title',
            'picture',
            'location1',
            'location2',
            'location3',
            'category'
        )
