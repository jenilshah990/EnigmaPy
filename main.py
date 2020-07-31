from Enigma import Enigma
from rotor import rotorDict
import error

# Input PlugBoard
plugboard = input('Input Plugboard Settings: ')
rotor1 = input('Input Rotor 1: ')
rotor2 = input('Input Rotor 2: ')
rotor3 = input('Input Rotor 3: ')
        
while True:
    try:
        notch_setting = input('Input Notch Settings: ')
        if len(notch_setting) != 3:
            raise error.NotchError
        else:
            break
    except error.NotchError:
        print('3 Notches not entered. Enter three notch values in the form ABC')


while True:
    ring_setting = input('Input Ring Settings: ')
    if len(ring_setting) != 3:
        print('Enter three ring values in the form ABC')
    else:
        break

reflector = input('Input Relfector Settings: ')

try:
    machine = Enigma(plugboard, reflector, rotor1, rotor2, rotor3, ring_setting, notch_setting)
except ValueError:
    print('The current configuration cannot make an Enigma Machine')

while True:
    print(machine.cipher(input('Enter Plaintext: ')))
    if input('Cipher new plaintext? (yes/no): ').upper() == 'NO':
        break
    else:
        continue
