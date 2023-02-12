from django.test import TestCase,Client

# Create your tests here.
class testing(TestCase):
    def setUp(self) -> None:
        self.client=Client()
    def test_login_user_view(self):
        response=self.client.get('/members/login_user')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'authenticate/login.html')
    def test_register_view(self):
        response=self.client.get('/members/register')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'register.html')
    
   