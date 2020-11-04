import unittest
from API_Yandex_Disc import shelf


class TestSomething(unittest.TestCase):
    def setUp(self):
        print("method setUp")

    def test_yandex_disk_folder(self):
        folder = shelf()
        self.assertEqual(folder, 201, 'Папка уже создана.')

    def test_yandex_disk_folder_error(self):
        error = shelf()
        self.assertEqual(error, 201, 'Папка уже создана.')

    def tearDown(self):
        print("method tearDown")


if __name__ == '__main__':
    unittest.main()
