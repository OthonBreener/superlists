from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_direciona_para_a_rota_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    
    
    def test_home_page_retorna_o_html_correto(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf-8')

        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))