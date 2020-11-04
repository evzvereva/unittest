import unittest
from unittest.mock import patch
from documents_and_directories import delete_a_document, add_a_document_to_the_shelf


class TestSomething(unittest.TestCase):
    def setUp(self):
        print("method setUp")

    @patch('builtins.input', side_effect=['10006', '3'])
    def test_move_document(self, directories):
        doc_number = delete_a_document()
        self.assertEqual(doc_number, 'Номер документа 10006 удален из полки № 2.')

    @patch('builtins.input', side_effect=['10006', '3'])
    def test_shelf(self, sh):
        number_of_shelf = add_a_document_to_the_shelf()
        self.assertEqual(number_of_shelf, 'Номер документа 10006 добавлен на полку № 3.')

    def tearDown(self):
        print("method tearDown")


if __name__ == '__main__':
    unittest.main()
