from rest_framework.viewsets import ModelViewSet
from profiles.models import *
from profiles.serializers import *

class UserProfileViewSet(ModelViewSet):
    """
    A viewset for CRUD operations over UserProfile model.
    """
    queryset=UserProfile.objects.all()
    serializer_class=UserProfileSerializer
