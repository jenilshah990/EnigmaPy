#ENIGMA_I Rotor Configurations
ROTOR_I = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
ROTOR_II = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
ROTOR_III = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]

class rotor(object):
    def __init__(self, shift, ring, notch, pos, next = None, wiring=None):
        if wiring == 'ROTOR_I':
            self.wiring = ROTOR_I
        elif wiring == 'ROTOR_II':
            self.wiring = ROTOR_II
        elif wiring == 'ROTOR_III':
            self.wiring = ROTOR_III
        else:
            self.wiring = wiring
        self.next = next
        self.pos = pos
        self.window = ord(ring) - ord('A')
        self.shift = shift
        self.rotations = 0
        self.notch = ord(notch.upper()) - ord('A')

    def encrypt(self, input):
        #Give input at Outer Ring
        if self.pos == 1:
            outer_ring = (self.window + input + 1) % 26
        else:
            outer_ring = input

        #Getting the inner ring letter through the wiring
        inner_ring = self.wiring[outer_ring]

        # Hitting the notch
        if self.window == self.notch and self.next != None:
            self.shift = self.shift + 1
            self.next.window = self.next.window + 1
            self.next.rotations = self.next.rotations + 1
            #self.next.shift = self.next.shift - 1

        if self.pos == 1:
            self.window += 1
            self.rotations = self.rotations + 1

        # getting the final output from the inner ring
        output = (inner_ring + self.shift - self.rotations) % 26
        return output

