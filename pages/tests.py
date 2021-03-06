from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from diary.models import Dairy
from django.contrib.auth import get_user_model
# Create your tests here.

class TestPages(SimpleTestCase):
    def test_home_page(self):
        response_home = self.client.get('/')
        response_dairy = self.client.get(reverse('create'))
        response_templates = self.client.get(reverse('home'))
        response_error = self.client.get('/homepage/')
        self.assertEqual(response_home.status_code,200)
        self.assertEqual(response_dairy.status_code,302)
        self.assertTemplateUsed(response_templates,'home.html')
        self.assertEqual(response_error.status_code,404)

class TestModels(TestCase):
    def test_model_object(self):
        get_user_model().objects.create_user({
            'username':'rukesh',
            'email':'rukesh.shrestha@heraldcollege.edu.np',
            'age':23,
            'password':'hahahaha'
        }
        )

        Dairy.objects.create(body='hey this is test.')
        data=Dairy.objects.get(pk=1)
        expected_object = data.body
        self.assertEqual(expected_object,'hey this is test.')