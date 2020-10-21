from django.test import TestCase
from django.core.exceptions import ValidationError
from profiles.models import UserProfile
from datetime import date

USER_FIRSTNAME="Test"
USER_LASTNAME="User"
USER_BIRTHDATE=date(1980,7,21)


class UserProfileModelTest(TestCase):
    def setUp(self):
        UserProfile.objects.create(
            firstname=USER_FIRSTNAME, 
            lastname=USER_LASTNAME, 
            birthdate=USER_BIRTHDATE
        )
    
    def test_fullname(self):
        """Test if fullname is generated correctly"""
        user = UserProfile.objects.get(firstname=USER_FIRSTNAME)
        fullname = USER_FIRSTNAME + " " + USER_LASTNAME
        self.assertEqual(fullname, user.fullname)
    
    def test_age(self):
        user = UserProfile.objects.get(firstname=USER_FIRSTNAME)
        self.assertEqual(40, user.age)
    
    def test_create_with_future_birtdate(self):
        with self.assertRaises(ValidationError):
            user = UserProfile.objects.create(
                firstname=USER_FIRSTNAME, 
                lastname=USER_LASTNAME, 
                birthdate=date(2025,10,21)
            )
            user.full_clean()

