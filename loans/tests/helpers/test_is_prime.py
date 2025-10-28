from django.test import TestCase
from loans.helpers import is_prime

# Create your tests here.

class IsPrimeTestCase(TestCase):
    def test_is_3_prime(self):
        result = is_prime(3)
        self.assertTrue(result)

    def test_is_1_prime(self):
        result = is_prime(1)
        self.assertFalse(result)

    def test_is_9_prime(self):
        result = is_prime(9)
        self.assertFalse(result)

    def test_is_2017_prime(self):
        result = is_prime(2017)
        self.assertTrue(result)

    def test_is_44_prime(self):
        result = is_prime(44)
        self.assertFalse(result)

    def test_is_2_prime(self):
        result = is_prime(2)
        self.assertTrue(result)

    def test_is_negative(self):
        with self.assertRaises(ValueError):
            result = is_prime(-2)
