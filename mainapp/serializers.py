from rest_framework import serializers

from mainapp.models import Item, Category


class ItemSerializer(serializers.ModelSerializer):
    category_title = serializers.ReadOnlyField(
        source='category.title'
    )

    class Meta:
        model = Item
        fields = (
            'id',
            'title',
            'category',
            'category_title',
            'date',
            'picture',
            'geotag',
            'description',
            'pickup_location',
            'is_lost'
        )

        extra_kwargs = {
            'category': {'write_only': True}
        }


class CategorySerializer(serializers.ModelSerializer):
    items = ItemSerializer(
        read_only=True, 
        many=True
    )

    class Meta:
        model = Category
        fields = (
            'id', 
            'title',
            'items'
        )


# class LostItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LostItem
#         fields = (
#             'title',
#             'picture',
#             'location1',
#             'location2',
#             'location3',
#             'category'
#         )
