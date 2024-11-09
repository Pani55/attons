from datetime import datetime

from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from sales_network.models import NetworkObject, Product
from users.models import User


class NetworkObjectTestCaseNotAuth(APITestCase):
    """ NetworkObject test case without authentication """

    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            model="Test_model",
            date_of_release=datetime.now()
        )
        self.network_object = NetworkObject.objects.create(
            name="Test Network Object",
            email="test@example.com",
            country="Test_country",
            city="Test_city",
            street="Test_street",
            house_number="Test_house_number",
            debt=0.0,
            supplier=None,
        )
        self.data = {
            "name": "Test Network Object 2",
            "email": "Test@mail.ku",
            "country": "Test_country2",
            "city": "Test_city2",
            "street": "Test_street2",
            "house_number": "Test_house_number2",
            "debt": 250000.0,
            "supplier": 1,   # Supplier ID
            "products": [1]  # Product ID
        }

    def test_network_object_create(self):
        """ Create a network object """

        url = reverse("sales_network:network_object_create")
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(NetworkObject.objects.count(), 1)

    def test_network_object_list(self):
        """ Test the network object list """

        url = reverse("sales_network:network_object_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(len(response.json()), 1)

    def test_network_object_update(self):
        """ Test network object update """

        url = reverse("sales_network:network_object_update", args=[self.network_object.id])
        response = self.client.put(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.network_object.refresh_from_db()
        self.assertEqual(self.network_object.name, "Test Network Object")

    def test_network_object_destroy(self):
        """ Test network object destroy """

        url = reverse("sales_network:network_object_destroy", args=[self.network_object.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(NetworkObject.objects.count(), 1)

    def test_network_object_retrieve(self):
        """ Test retrieve view network object """

        url = reverse("sales_network:network_object_retrieve", args=[self.network_object.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class NetworkObjectTestCaseWithAuth(APITestCase):
    """ Network object test case with authentication """

    def setUp(self):
        self.user = User.objects.create(email="admin@example.com", password="123666")
        self.product = Product.objects.create(
            name="Test Product",
            model="Test_model",
            date_of_release=datetime.now()
        )
        self.data = {
            "name": "Test Network Object 2",
            "email": "Test@mail.ku",
            "country": "Test_country2",
            "city": "Test_city2",
            "street": "Test_street2",
            "house_number": "Test_house_number2",
            "debt": 250000.0,
            "products": [self.product.pk]
        }
        self.network_object = NetworkObject.objects.create(
            name="Test Network Object",
            email="test@example.com",
            country="Test_country",
            city="Test_city",
            street="Test_street",
            house_number="Test_house_number",
            debt=0.0,
            supplier=None,
        )
        self.client.force_authenticate(user=self.user)

    def test_network_object_create(self):
        """ Create a network object """

        url = reverse("sales_network:network_object_create")
        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(NetworkObject.objects.count(), 2)

    def test_network_object_list(self):
        """ Test list of network objects """

        url = reverse("sales_network:network_object_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_network_object_update(self):
        """ Test network object update """

        url = reverse("sales_network:network_object_update", args=[self.network_object.id])
        response = self.client.put(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.network_object.refresh_from_db()
        self.assertEqual(self.network_object.name, "Test Network Object 2")

    def test_network_object_destroy(self):
        """ Test network object destroy """

        url = reverse("sales_network:network_object_destroy", args=[self.network_object.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(NetworkObject.objects.count(), 0)

    def test_network_object_retrieve(self):
        """ Test retrieve network object """

        url = reverse("sales_network:network_object_retrieve", args=[self.network_object.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
