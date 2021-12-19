from django.test import TestCase
from django.urls import resolve

# Create your tests here.

class HomePageTest(TestCase):
    
    def test_home_page_retorna_o_html_correto(self):
        
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')