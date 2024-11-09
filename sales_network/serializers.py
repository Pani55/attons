from rest_framework.serializers import ModelSerializer
from sales_network.models import Product, NetworkObject


class ProductSerializer(ModelSerializer):
    """ Serializer for Product objects. """

    class Meta:
        model = Product
        fields = "__all__"


class NetworkObjectSerializer(ModelSerializer):
    """ Serializer for Network objects. """

    class Meta:
        model = NetworkObject
        fields = "__all__"


class NetworkObjectUpdateSerializer(ModelSerializer):
    """ Serializer for Network objects with excluding 'debt' line. """

    class Meta:
        model = NetworkObject
        exclude = ["debt",]
