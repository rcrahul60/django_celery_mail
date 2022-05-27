from django.urls import reverse
from django.test import TestCase
from ..models import CustomUser

# Create your tests here.

class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_number=5
        for user_id in range(user_number):
            CustomUser.objects.create(name=f"testuser{user_id}",email=f"testuser{user_id}@mail.com",password="test@123")
        pass

    # def setUp(self):
    #     print("setUp: Run once for every test method to setup clean data.")
    #     pass

    def test_url_exists(self):
        response = self.client.get("/api/v1.0/user/list/")
        self.assertEqual(response.status_code,200)

    def test_url_accessible_by_name(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code,200)
        
    # def test_false_is_false(self):
    #     print("Method: test_false_is_false.")
    #     self.assertFalse(False)

    # def test_false_is_true(self):
    #     print("Method: test_false_is_true.")
    #     self.assertTrue(False)

    # def test_one_plus_one_equals_two(self):
    #     print("Method: test_one_plus_one_equals_two.")
    #     self.assertEqual(1 + 1, 2)