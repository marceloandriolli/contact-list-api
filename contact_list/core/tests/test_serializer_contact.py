from django.test import TestCase

from core.models import Contact
from core.serializers import ContactSerializer


class ContactSerializerTest(TestCase):
    def setUp(self):
        self.contact_attributes = {
            'name': 'Marcelo Andriolli',
            'email': 'marcelorsa@gmail.com',
            'phone': '48-99627-4443' 
        }
        self.serialize_data = {
            'name': 'Marcelo Andriolli',
            'email': 'marcelorsa@gmail.com',
            'phone': '48-99627-4443' 
        }
        self.contact = Contact.objects.create(**self.contact_attributes)
        self.serializer = ContactSerializer(instance=self.contact)
        self.data = self.serializer.data

    def test_contains_expected_fields(self):
        self.assertEqual(set(self.data.keys()), set(['name', 'email', 'phone']))
    
    def test_contains_expected_content(self):
        self.assertDictEqual(self.data, self.contact_attributes)
