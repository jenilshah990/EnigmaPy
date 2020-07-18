#ENIGMA_I Rotor Configurations
ROTOR_I = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
ROTOR_II = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
ROTOR_III = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]



class rotor():
    def __init__(self, key, notch):
        #Offset Calculations
        self.off1 = ord(key[0].upper())-ord('A') #off1 = ring setting 1
        self.off2 = (ord(key[1].upper())-ord(key[0].upper()))%26 #off2 = ring setting 2 - ring setting 1
        self.off3 = (ord(key[2].upper())-ord(key[1].upper()))%26 #off3 = ring setting 3 - ring setting 2
        self.off4 = (ord('A')-ord(key[2].upper()))%26 #off4 = ring setting 3

        #Window & Notch Calculations
        self.window1 = ord(key[0].upper())-ord('A') #Index of the Letter that appers on the Window of ROTORI
        self.window2 = ord(key[1].upper()) - ord('A') #Index of the Letter that appers on the Window of ROTORI
        self.notch1 = ord(notch[0].upper())-ord('A') #Index of Notch of Rotor I
        self.notch2 = ord(notch[1].upper())-ord('A') #Index of Notch of Rotor II

    def notch(self):
        #Notch II hits after Notch I
        if self.window2 == self.notch2:
            self.off2 = (self.off2+1)%26
            self.off4 = (self.off4-1)%26
            self.window2 = (self.window2+1)%26

        #Only Notch I hits
        #window1 == off1 - 1 here
        elif self.window1 == self.notch1:
            self.off2 = (self.off2+1)%26
            self.off3 = (self.off3-1)%26

    #Encrpytion while going forward
    def encrypt_forward(self, input):
        #Rotation
        self.off1 = (self.off1+1)%26
        self.off2 = (self.off2-1)%26
        #Encrytion
        self.notch()
        outer_ring_1 = (input + self.off1)%26
        inner_ring_1 = ROTOR_I[outer_ring_1]
        outer_ring_2 = (inner_ring_1 + self.off2)%26
        inner_ring_2 = ROTOR_II[outer_ring_2]
        outer_ring_3 = (inner_ring_2 + self.off3)%26
        inner_ring_3 = ROTOR_III[outer_ring_3]
        output = (inner_ring_3 + self.off4)%26
        self.window1 = (self.window1 + 1)%26
        return output

    #Encryption after returning from Reflector
    def encrpyt_backward(self, input):
        input = (input - self.off4)%26
        input = ROTOR_III.index(input)
        input = (input - self.off3)%26
        input = ROTOR_II.index(input)
        input = (input - self.off2) % 26
        input = ROTOR_I.index(input)
        input = (input - self.off1) % 26
        return input