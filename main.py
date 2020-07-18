import plugboard
import rotor
import reflector
import rotor1

#PlugBoard testing
x = plugboard.plugboard('AB CD EF GH IJ')
r = x.plugboard_encrypt(1)

#Helper: Creating Rotor wirings list from strings
wiring = list(range(26))
s = list('UQNTLSZFMREHDPXKIBVYGJCWOA')
i = 0
for c in s:
    letter_index = ord(c)-ord('A')
    wiring[i]=letter_index
    i=i+1
print(wiring)
#Enigma Class: Rotor Testing
class Enigma:
    def __init__(self, ring_settings, notch_settings):
        shift1 = (ord(ring_settings[1]) - ord(ring_settings[0]))%26
        shift2 = (ord(ring_settings[2]) - ord(ring_settings[1]))%26
        shift3 = (ord('A') - ord(ring_settings[2]))%26
        self.rotor3 = rotor.rotor(shift3, ring_settings[2], notch_settings[2], 3, None, 'ROTOR_III')
        self.rotor2 = rotor.rotor(shift2, ring_settings[1], notch_settings[1], 2, self.rotor3, 'ROTOR_II')
        self.rotor1 = rotor.rotor(shift1, ring_settings[0], notch_settings[0], 1, self.rotor2, 'ROTOR_I')
        rotors = [0, self.rotor1, self.rotor2,self.rotor3]

    def encrypt(self, input):
        out1 = self.rotor1.encrypt(input)
        print(out1)
        out2 = self.rotor2.encrypt(out1)
        print(out2)
        output = self.rotor3.encrypt(out2)
        print(output)

A = Enigma('QDC', 'QEJ')
A.encrypt(0)

#Reflector Testing
R = reflector.reflector('AB CD EF GH IJ')
print(R.encrypt(0))

#Rotor Testing
R = rotor1.rotor('QED', 'QE')
print(R.encrypt_forward(1))
print(R.encrpyt_backward(16))

