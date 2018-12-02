# coding=utf-8

from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class Index_view_teste_casa(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('index-light')

    def tearDown(self):
        pass


    def teste_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_template_user(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, 'index-light.html')