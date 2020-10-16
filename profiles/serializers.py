from rest_framework.serializers import ModelSerializer
from profiles.models import *

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
