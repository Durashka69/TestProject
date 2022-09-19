from rest_framework.routers import DefaultRouter

from mainapp.views import (
    CategoryViewSet, FoundItemViewSet, LostItemViewSet
)

router = DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('found-items', FoundItemViewSet)
router.register('lost-items', LostItemViewSet)

urlpatterns = []

urlpatterns += router.urls
