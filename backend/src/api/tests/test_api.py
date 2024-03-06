from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
import time


class TestGetAllData(APITestCase):

    endpoint='/api/v1/get-data'

    def test_get_data(self):
        resp=self.client.get(self.endpoint)
        res=resp.json()
        self.assertEqual(first=resp.status_code,second=status.HTTP_200_OK)
        self.assertDictEqual(d1=res,d2={"data":[]})
