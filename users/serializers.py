from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """ Serializer for users. """

    class Meta:
        model = User
        fields = "__all__"
