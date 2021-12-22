from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()


    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_restrieve_it_later(self):
        # Edith ouviu falar em uma nova aplicacao online interessante
        # Para a lista de tarefas ela decidide verificar sua homepage
        self.browser.get("http:localhost:8000")

        # Ela percebe que o titulo da pagina e o cabecalho mencionam
        # listas de tarefas to-do
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test")

        # Ela e convidada a inserir um item de tarefa imediatamente

if __name__ == '__main__':
    unittest.main(warnings='ignore')
