#ENIGMA_I Rotor Configurations
ROTOR_I = [5, 11, 13, 6, 12, 7, 4, 17, 22, 26, 14, 20, 15, 23, 25, 8, 24, 21, 19, 16, 1, 9, 2, 18, 3, 10]
ROTOR_II = [1, 10, 4, 11, 19, 9, 18, 21, 24, 2, 12, 8, 23, 20, 13, 3, 17, 7, 26, 14, 16, 25, 6, 22, 15, 5]
ROTOR_III = [2, 4, 6, 8, 10, 12, 3, 16, 18, 20, 24, 22, 26, 14, 25, 5, 9, 23, 7, 1, 11, 13, 21, 19, 17, 15]

class rotor(object):
    def __init__(self, state, notch, wiring=None):
        if wiring == 'ROTOR_I':
            self.wiring = ROTOR_I
        else:
            self.wiring = wiring
        self.window = ord(state[0]) - ord('A')
        self.state = state
        self.rotations = 0
        self.shift = (ord(self.state[1].upper()) - ord('A') - ord(self.state[0].upper()) - ord('A'))%26
        self.notch = ord(notch.upper()) - ord('A')

    def encrypt(self, input):
        #Give input at Outer Ring
        outer_ring = (self.window + input) % 26

        #Represents rotation of the Rotor
        self.window += 1
        self.rotations = self.rotations+1


        #Getting the inner ring letter through the wiring
        inner_ring = self.wiring[outer_ring]

        #getting the final output from the inner ring
        output = (inner_ring + self.shift - self.rotations)%26

        #Hitting the notch
        if self.window == self.notch:
            self.shift = self.shift + 1
        return output

