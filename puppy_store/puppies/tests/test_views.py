from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import Puppy
from ..serializers import PuppySerializer
from rest_framework import status

class ListPuppies(APITestCase):

    def setUp(self):
        Puppy.objects.create(name='Eddi', age=2, breed='Siberian Husky', color='Black & White')
        Puppy.objects.create(name='Scooby', age=10, breed='Sepa la chingada', color='Brown')
        Puppy.objects.create(name='Coraje', age=100, breed='Cobarde', color='Pink')
        Puppy.objects.create(name='Otro Wey', age=1, breed='Wey', color='Pink')

    def test_list_all_puppies_ok(self):
        response = self.client.get(reverse('puppies'))
        puppies = Puppy.objects.all()
        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_all_red_puppies_ok(self):
        response = self.client.get(f'{reverse("puppies")}?color=Pink')
        puppies = Puppy.objects.filter(color='Pink')
        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_not_found_ok(self):
        response = self.client.get(f'{reverse("puppies")}?color=Verde')
        puppies = Puppy.objects.filter(color='Verde')
        serializer = PuppySerializer(puppies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
