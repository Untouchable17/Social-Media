from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class BlogApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('blogs_list')
        print(url)
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        print(response.data)