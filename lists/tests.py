from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_direciona_para_a_rota_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)