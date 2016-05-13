import string


class CaesarCipher:
    def __init__(self, key):
        self.alphabet = string.ascii_lowercase
        self.shiftedAlphabet = self.alphabet[key:] + self.alphabet[:key]

    def encrypt(self, message):
        encryptedMessage = ''
        for character in message:
            if (character.isspace()):
                encryptedMessage += " "
            else:
                index = self.alphabet.index(character)
                encryptedMessage += self.shiftedAlphabet[index]
        return encryptedMessage

    def decrypt(self, message):
        decryptedMessage = ''
        for character in message:
            if (character.isspace()):
                decryptedMessage += " "
            else:
                index = self.shiftedAlphabet.index(character)
                decryptedMessage += self.alphabet[index]
        return decryptedMessage