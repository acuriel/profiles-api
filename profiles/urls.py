from django.urls import path
from rest_framework.routers import DefaultRouter
from profiles.views import *

router = DefaultRouter()
router.register(r'', UserProfileViewSet, basename='profile')
urlpatterns = router.urls
