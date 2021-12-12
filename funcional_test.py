from selenium import webdriver
import unittest

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
        """
        Ela é convidada a inserir um item de tarefa imediatamente.

        Ela digita 'Comprar penas de urubu' em uma caixa de texto.

        Quando ela tecla enter, a página é atualizada, e agora a página
        lista:
            1). Comprar penas de urubu
        como um item em uma lista de tarefas.

        Ainda continua havendo uma caixa de texto convidando-a a acrescentar
        outro item. Ela insere: 'Rabo de Galinha'.

        A página é atualizada novamente e agora mostra os dois itens em sua lista.

        Sheila se pergunta se o site lembrará de sua lista. Então ela nota que o site
        gerou um url único para ela. Ela acessa esse url e sua lista de tarefas continua lá.
        """
        self.fail('Fim do Teste')
    
if __name__ == '__main__':
    unittest.main(warnings='ignore')



