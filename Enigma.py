from plugboard import plugboard
from rotor import rotor

class Enigma():
    # Create a PlugBoard, Rotors & Reflector
    def __init__(self, plugboard_settings, reflector_settings, rotor1, rotor2, rotor3, ring_settings, notch_settings):
        self.plug_board = plugboard(plugboard_settings, 0)
        self.rotor = rotor(ring_settings, notch_settings, rotor1, rotor2, rotor3)
        self.reflector = plugboard(reflector_settings, 1)

    def encrypt(self, plaintext):
        ciphertext = ''
        for c in plaintext:
            letter_index = ord(c.upper())-ord('A')
            letter_index = self.p_board.plugboard_encrypt(letter_index)
            letter_index = self.rotor.encrypt_forward(letter_index)
            letter_index = self.reflector.plugboard_encrypt(letter_index)
            letter_index = self.rotor.encrpyt_backward(letter_index)
            letter_index = self.p_board.plugboard_encrypt(letter_index)
            ciphertext += chr(letter_index + ord('A'))
        return ciphertext



