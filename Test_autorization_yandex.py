import unittest
from autorizatoin_yandex_email_selenium import login_with, login_yandex_email, password_yandex


class TestSomething(unittest.TestCase):
    def setUp(self):
        print("method setUp")

    def test_login_with(self):
        login_and_password = login_with(login_yandex_email, password_yandex)
        self.assertEqual(login_and_password, 'evzvereva.python@yandex.ru, EVZVEREVA')

    def tearDown(self):
        print("method tearDown")


if __name__ == '__main__':
    unittest.main()
