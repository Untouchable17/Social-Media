from django.test import TestCase
from django.urls import reverse

from rest_framework import status


class ViewApiTestCase(TestCase):
    def test_user_contact(self):
        url = reverse('send_mail')
        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_post_create(self):
        url = reverse('blogs_list')
        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)