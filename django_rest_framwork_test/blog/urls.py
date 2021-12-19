from rest_framework import routers

from .views import EntryViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"entries", EntryViewSet)
