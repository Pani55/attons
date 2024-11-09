from rest_framework.routers import SimpleRouter
from sales_network.apps import SalesNetworkConfig
from django.urls import path
from sales_network.views import (NetworkObjectCreateAPIView, NetworkObjectListAPIView,
                                 NetworkObjectUpdateAPIView, NetworkObjectDestroyAPIView,
                                 ProductViewSet, NetworkObjectRetrieveAPIView)

app_name = SalesNetworkConfig.name

router = SimpleRouter()
router.register("", ProductViewSet)

urlpatterns = [
    path("create/", NetworkObjectCreateAPIView.as_view(), name="network_object_create"),
    path("list/", NetworkObjectListAPIView.as_view(), name="network_object_list"),
    path("update/<int:pk>/", NetworkObjectUpdateAPIView.as_view(), name="network_object_update"),
    path("destroy/<int:pk>/", NetworkObjectDestroyAPIView.as_view(), name="network_object_destroy"),
    path("retrieve/<int:pk>/", NetworkObjectRetrieveAPIView.as_view(), name="network_object_retrieve"),
]

urlpatterns += router.urls
