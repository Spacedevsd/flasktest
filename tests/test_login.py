import unittest

from app import create_app
from bs4 import BeautifulSoup


class LoginTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.context = self.app.app_context()
        self.context.push()
        self.client = self.app.test_client()

    def test_check_status_code_200_in_login_page(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 200)

    def test_check_exists_entrar_button_in_login_page(self):
        response = self.client.get("/login")
        self.assertIn("Entrar", response.get_data(as_text=True))

    def test_check_exists_registrar_button_in_login_page(self):
        response = self.client.get("/login")
        self.assertIn("Registrar", response.get_data(as_text=True))

    def test_count_buttons_in_login_page(self):
        response = self.client.get("/login")
        html = response.get_data(as_text=True)

        soup = BeautifulSoup(html, "html.parser")
        buttons = soup.select("button") # ["<button>", "<button>"]

        self.assertEqual(len(buttons), 2)

    def test_login_via_post_with_data(self):
        payload = {
            "email": "oi@spacedevs.com.br",
            "password": "12345",
        }
        response = self.client.post("/login", data=payload)
        self.assertEqual(response.get_data(as_text=True), "Email: oi@spacedevs.com.br / password: 12345")
        
    def test_login_via_post_without_data(self):
        response = self.client.post("/login")
        self.assertEqual(response.get_data(as_text=True), "Os dados precisam ser inseridos")
    
    def test_exists_only_one_form_in_login_page(self):
        response = self.client.get("/login")

        html = response.get_data(as_text=True)
        soup = BeautifulSoup(html, "html.parser")

        form = soup.select("form[name=loginform]")

        self.assertEqual(len(form), 1)

    def tearDown(self) -> None:
        self.context.pop()