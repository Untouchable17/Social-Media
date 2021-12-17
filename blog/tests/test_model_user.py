from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status

User = get_user_model()


class ProfileTestCases(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username="testuser2", password="password2")
        self.image = SimpleUploadedFile("default.jpg", content=b'', content_type="image/jpg")

    def test_profile(self):
        url = reverse('blogs_list')
        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(self.user, self.user)
