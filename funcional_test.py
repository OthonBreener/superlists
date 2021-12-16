import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path=r'C:\Users\othon\Documents\geckodriver.exe')
        self.url = 'http://localhost:8000'

    def tearDown(self):
        self.browser.quit()
    
    def test_abrir_uma_lista_de_tarefas(self):
        """
        Sheila ouviu sobre uma nova aplicação online interessante para 
        lista de tarefas. Ela decide verificar na sua homepage
        """
        self.browser.get(self.url)
        """
        Ela percebe que o titula da página e o cabeçalho mencionam listas
        de tarefas (to-do)
        """
        self.assertIn('To-Do', self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        
        self.assertIn('To-Do', header_text)
        """
        Ela é convidada a inserir um item de tarefa imediatamente.

        """
        inputbox = self.browser.find_element_by_id('id_new_item')

        self.assertEqual(inputbox.get_attribute('placeholder'), 'Digite uma tarefa')

        """

        Ela digita 'Comprar penas de urubu' em uma caixa de texto.
        """
        inputbox.send_keys('Comprar penas de urubu')

        """
        Quando ela tecla enter, a página é atualizada, e agora a página
        lista:
            1). Comprar penas de urubu
        como um item em uma lista de tarefas.
        """
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1). Comprar penas de urubu' for row in rows)
        )

        """
        Ainda continua havendo uma caixa de texto convidando-a a acrescentar
        outro item. Ela insere: 'Rabo de Galinha'.

        A página é atualizada novamente e agora mostra os dois itens em sua lista.

        Sheila se pergunta se o site lembrará de sua lista. Então ela nota que o site
        gerou um url único para ela. Ela acessa esse url e sua lista de tarefas continua lá.
        """
        self.fail('Termine o Teste')
    
if __name__ == '__main__':
    unittest.main(warnings='ignore')



