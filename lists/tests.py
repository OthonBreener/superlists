from django.test import TestCase

# Create your tests here.

class SmokeTest(TestCase):

    def test_qualquer_para_verificar_o_teste_do_django(self):
        self.assertEqual(1+1, 3)