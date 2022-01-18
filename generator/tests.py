import json
import uuid
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class VaultTest(APITestCase):

    def test_generate_uuid(self):
        """
        Tests that a new UUID is generated and returns previously
        created generated UUIDs.
        """
        url = reverse('uuid-generator')
        data = {}

        response = self.client.post(url, data, format='json')
        response_data = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response_data), 1)

        response = self.client.post(url, data, format='json')
        response = self.client.post(url, data, format='json')
        response = self.client.post(url, data, format='json')
        response_data = json.loads(response.content)

        self.assertEqual(len(response_data), 4)
