#ENIGMA_I Rotor Wi
ROTOR_I = [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
ROTOR_II = [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
ROTOR_III = [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]

#ENIGMA IC Rotors Wis
ROTOR_IC = [3, 12, 19, 22, 18, 8, 11, 17, 20, 24, 16, 13, 10, 5, 4, 9, 2, 0, 25, 1, 15, 6, 23, 14, 7, 21]
ROTOR_IIC = [7, 16, 25, 6, 15, 9, 19, 12, 14, 1, 11, 13, 2, 8, 5, 3, 24, 0, 22, 21, 4, 20, 18, 17, 10, 23]
ROTOR_IIIC = [20, 16, 13, 19, 11, 18, 25, 5, 12, 17, 4, 7, 3, 15, 23, 10, 8, 1, 21, 24, 6, 9, 2, 22, 14, 0]

dict = {'ROTOR_I': ROTOR_I, 'ROTOR_II':ROTOR_II, 'ROTOR_III':ROTOR_III}

class rotor():
    def __init__(self, ring, notch, rotor1, rotor2, rotor3):
        if rotor1 in dict:
            self.rotor1 = dict[rotor1]
        if rotor2 in dict:
            self.rotor2 = dict[rotor2]
        if rotor3 in dict:
            self.rotor3 = dict[rotor3]

        #Offset Calculations
        self.off1 = ord(ring[0].upper())-ord('A') #off1 =  setting 1
        self.off2 = (ord(ring[1].upper())-ord(ring[0].upper()))%26 #off2 =  setting 2 -  setting 1
        self.off3 = (ord(ring[2].upper())-ord(ring[1].upper()))%26 #off3 =  setting 3 -  setting 2
        self.off4 = (ord('A')-ord(ring[2].upper()))%26 #off4 =  setting 3

        #Window & Notch Calculations
        self.window1 = ord(ring[0].upper())-ord('A') #Index of the Letter that appers on the Window of ROTORI
        self.window2 = ord(ring[1].upper()) - ord('A') #Index of the Letter that appers on the Window of ROTORI
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
        outer__1 = (input + self.off1)%26
        inner__1 = self.rotor1[outer__1]
        outer__2 = (inner__1 + self.off2)%26
        inner__2 = self.rotor2[outer__2]
        outer__3 = (inner__2 + self.off3)%26
        inner__3 = self.rotor3[outer__3]
        output = (inner__3 + self.off4)%26
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