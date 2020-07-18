from plugboard import plugboard
from reflector import reflector
from rotor1 import rotor
import keyboard

class Enigma():
    # Create a PlugBoard, Rotors & Reflector
    def __init__(self, plugboard_settings, reflector_settings, rotor1, rotor2, rotor3, ring_settings, notch_settings):
        self.p_board = plugboard(plugboard_settings)
        self.rotor = rotor(ring_settings, notch_settings, rotor1, rotor2, rotor3)
        self.reflector = plugboard(reflector_settings)

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

A = Enigma('AR BJ ST', 'AY BR CU DH EQ FS GL IP JX KN MO TZ VW','ROTOR_I', 'ROTOR_II', 'ROTOR_III', 'QEV', 'QE')

s = keyboard.record(until = 'Esc')
s = A.encrypt(s)
keyboard.play(s, speed_factor = 1)

'''
cipher = A.encrypt(input('Input Plaintext: '))
print(cipher)
'''


