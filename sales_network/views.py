from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter

from sales_network.models import NetworkObject, Product
from sales_network.paginations import ObjectListPagination
from sales_network.serializers import (NetworkObjectSerializer, ProductSerializer,
                                       NetworkObjectUpdateSerializer)


# Create your views here.
class NetworkObjectCreateAPIView(generics.CreateAPIView):
    """ Create a network object. """

    serializer_class = NetworkObjectSerializer
    queryset = NetworkObject.objects.all()


class NetworkObjectListAPIView(generics.ListAPIView):
    """ View for a list of network objects. """

    serializer_class = NetworkObjectSerializer
    queryset = NetworkObject.objects.all()
    pagination_class = ObjectListPagination

    filter_backends = (SearchFilter,)
    search_fields = ["country"]


class NetworkObjectRetrieveAPIView(generics.RetrieveAPIView):
    """ Retrieves information about a network object. """

    serializer_class = NetworkObjectSerializer
    queryset = NetworkObject.objects.all()


class NetworkObjectUpdateAPIView(generics.UpdateAPIView):
    """ Update network object. Cannot update 'debt' line. """

    serializer_class = NetworkObjectUpdateSerializer
    queryset = NetworkObject.objects.all()


class NetworkObjectDestroyAPIView(generics.DestroyAPIView):
    """ View to destroy a network object. """

    queryset = NetworkObject.objects.all()
    serializer_class = NetworkObjectSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """ Viewset for product. Including all of CRUD operations. """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ObjectListPagination
