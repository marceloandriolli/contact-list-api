from django.test import TestCase
from core.models import Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.obj = Contact(
            name='Marcelo Andriolli',
            email='marcelorsa@gmail.com',
            phone='48-996274443'
        )
        self.obj.save()
    
    def test_create(self):
        self.assertTrue(Contact.objects.exists())
    
    def test_get(self):
        contact = Contact.objects.get(name='Marcelo Andriolli')
        self.assertTrue(self.obj.name, contact.name)

    def test_update(self):
        expected = 'marceloandriolli@gmail.com'
        self.obj.email = expected
        self.obj.save()
        self.assertTrue(expected, self.obj.email)

    def test_delete(self):
        Contact.objects.filter(name='Marcelo Andriolli').delete()
        self.assertFalse(Contact.objects.exists())

    