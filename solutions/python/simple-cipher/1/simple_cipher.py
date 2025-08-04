import string
import random

class Cipher:
    def __init__(self, key=None):
        if key is None:
            key = ""
            for i in range(100):
                key += random.choice(string.ascii_letters[0:26])
            print(key)

        self.key = key

    def encode(self, text):
        result = ""
        key_index = 0

        for letter in text:
            key_letter = self.key[key_index]
            encoded_letter_ord = ord(letter) + (ord(key_letter) - ord('a'))

            if encoded_letter_ord > ord('z'):
                encoded_letter_ord -= 26

            result += chr(encoded_letter_ord)

            key_index += 1
            if key_index >= len(self.key):
                key_index = 0
            
        return result

    def decode(self, text):
        result = ""
        key_index = 0

        for letter in text:
            key_letter = self.key[key_index]
            decoded_letter_ord = ord(letter) - (ord(key_letter) - ord('a'))

            if decoded_letter_ord < ord('a'):
                decoded_letter_ord += 26

            result += chr(decoded_letter_ord)

            key_index += 1
            if key_index >= len(self.key):
                key_index = 0
            
        return result