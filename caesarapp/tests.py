from django.test import TestCase

# Create your tests here.
from django.utils.crypto import random

from caesarapp.CaesarCipher import CaesarCipher


class CaesarCipherTestCase(TestCase):
    def setUp(self):
        key = random.randrange(0, 100)
        self.message = "onelowercaseword"
        self.testCipher = CaesarCipher(key)

    def test_encrypt_decrypt(self):
        encrypted = self.testCipher.encrypt(self.message)
        decrypted = self.testCipher.decrypt(encrypted)
        self.assertEqual(self.message, decrypted)