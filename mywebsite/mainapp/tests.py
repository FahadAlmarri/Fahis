from django.test import TestCase,Client
from . import views
# Create your tests here.
class testing(TestCase):
    def setUp(self) -> None:
        self.client=Client()
    def test_home_view(self):
        response=self.client.get('/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'frontend/index.html')
    def test_history_view(self):
        response=self.client.get('/history')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'frontend/history.html')
   