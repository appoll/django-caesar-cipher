from django.db import models
from django.utils import timezone
# Create your models here.

class CaesarCipher:
    def __init__(self, key):
        self.alphabet = string.ascii_lowercase
        self.shiftedAlphabet = self.alphabet[key:] + self.alphabet[:key]

    def encrypt(self, message):
        encryptedMessage = ''
        for character in message:
            index = self.alphabet.index(character)
            encryptedMessage += self.shiftedAlphabet[index]
        return encryptedMessage

    def decrypt(self, message):
        decryptedMessage = ''
        for character in message:
            index = self.shiftedAlphabet.index(character)
            decryptedMessage += self.alphabet[index]
        return decryptedMessage


class UserInput(models.Model):
    plain_text = models.CharField(max_length=140)
    encryption_key = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.plain_text