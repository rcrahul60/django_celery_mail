from django.test import TestCase
from ..models import CustomUser

class UserModelTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        CustomUser.objects.create(name='john',email='john@mail.com',password='test@123')


    def test_string_method(self):
        user = CustomUser.objects.get(id=1)
        expected_string = f"{user.name}"
        self.assertEqual(str(user.name),expected_string)
