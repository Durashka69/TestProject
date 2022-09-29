from rest_framework.routers import DefaultRouter

from mainapp.views import (
    CategoryViewSet, ItemViewSet
)

router = DefaultRouter()

router.register('categories', CategoryViewSet)
router.register('items', ItemViewSet)
# router.register('lost-items', LostItemViewSet)

urlpatterns = []

urlpatterns += router.urls
