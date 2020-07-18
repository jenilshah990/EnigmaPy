#!/usr/bin/env python
#-*- coding: utf-8 -*-
Reflector_A = [4, 9, 12, 25, 0, 11, 24, 23, 21, 1, 22, 5, 2, 17, 16, 20, 14, 13, 19, 18, 15, 8, 10, 7, 6, 3]
Reflector_B = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
Reflector_C = [5, 21, 15, 9, 8, 0, 14, 24, 4, 3, 17, 25, 23, 22, 6, 2, 19, 10, 20, 16, 18, 1, 13, 12, 7, 11]

class plugboard():
    # Wires the plugboard from the settings provided in wiring_pairs
    def __init__(self, wiring_pairs,p):
        # Creating a default 1:1 wiring
            # for setA = EJMZALYXVBWFCRQUONTSPIKHGD         
        if wiring_pairs.upper() == 'REFLECTOR_A':
            self.wiring = Reflector_A
            
           # for setB = YRUHQSLDPXNGOKMIEBFZCWVJAT
        elif wiring_pairs.upper() == 'REFLECTOR_B':
            self.wiring = Reflector_B
            
            #for setC = FVPJIAOYEDRZXWGCTKUQSBNMHL
        elif wiring_pairs.upper() == 'REFLECTOR_C':
            self.wiring = Reflector_C
            
        else:
            assert (p==0 or p==1) , 'Error choose either plugborad or reflector'
            assert(len(set(''.join(wiring_pairs.split()))) == len(''.join(wiring_pairs.split()))), 'Custom Reflector Configuration should not have repeating characters'
            if p == 0:
                assert len(wiring_pairs.split())<=13 , 'Add only 13 or less pairs in form: AB CD EF ....YZ'
            else :
                assert len(wiring_pairs.split())==13 , 'Add exactly 13 wiring pairs in form : AB CD EF ....YZ'
                
            # Converts the writing_pairs in the form 'AJ RT PQ..' to '[(0,9), (16, 19)...] & then converts the wirings
            self.wiring = list(range(26))
            for p in wiring_pairs.upper().split():
                 m = ord(p[0]) - ord('A')
                 n = ord(p[1]) - ord('A')
                 self.wiring[m] = n
                 self.wiring[n] = m
    
    # The letter is encrypted according to wiring
    def plugboard_encrypt(self, letter):
        return self.wiring[letter]
