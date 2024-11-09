from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """ Create a new user """

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """ A new user is created with inactive status """

        user = serializer.save(is_active=False)
        user.set_password(user.password)
        user.save()


class UserListAPIView(ListAPIView):
    """ View for users list. """

    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    """ Update user information. """

    serializer_class = UserSerializer
    queryset = User.objects.all()
