from json import loads, dumps

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from core.models import Contact


class ContactViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('contact-list')
        self.data = {
            'name': 'Marcelo Andriolli',
            'email': 'marcelorsa@gmail.com',
            'phone': '48-996274443'
        }
        self.response = self.client.post(self.url, self.data, format='json')

    def test_create_contact(self):
        """ Must be create a new contact """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED) 
    
    def test_create_invalid_contact(self):
        self.data.pop('name', None)
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_list_contact(self):
        response = self.client.get(self.url)
        reposnse_data = loads(dumps(response.data[0]))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(self.data, reposnse_data)
    
    def test_get_contact(self):
        contact = Contact.objects.create(**self.data)
        url = reverse('contact-detail', kwargs={'pk': contact.pk})
        response = self.client.get(url)
        self.assertDictEqual(self.data, response.data)

    def test_get_invalid_contact(self):
        url = reverse('contact-detail', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_update_contact(self):
        contact = Contact.objects.create(**self.data)
        data = {
            'name': 'Marcelo Andriolli',
            'email': 'marcelorsa@gmail.com',
            'phone': '48-984234431'
        }
        
        url = reverse('contact-detail', kwargs={'pk': contact.pk})
        response = self.client.put(url,
                                   data=dumps(data),
                                   content_type='application/json')
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_update_invalid_contact(self):
        contact = Contact.objects.create(**self.data)
        data = {
            'phone': '48-996274443'
        }
        
        url = reverse('contact-detail', kwargs={'pk': contact.pk})
        response = self.client.put(url,
                                   data=dumps(data),
                                   content_type='application/json')
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_delete_contact(self):
        contact = Contact.objects.create(**self.data)
        url = reverse('contact-detail', kwargs={'pk': contact.pk})
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

    def test_delete_invalid_contact(self):
        url = reverse('contact-detail', kwargs={'pk': 23})
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_404_NOT_FOUND, response.status_code)
        



        

