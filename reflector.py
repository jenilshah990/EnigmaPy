#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 21:46:47 2020

@author: hetshah
"""
Reflector_A = [4, 9, 12, 25, 0, 11, 24, 23, 21, 1, 22, 5, 2, 17, 16, 20, 14, 13, 19, 18, 15, 8, 10, 7, 6, 3]
Reflector_B = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
Reflector_C = [5, 21, 15, 9, 8, 0, 14, 24, 4, 3, 17, 25, 23, 22, 6, 2, 19, 10, 20, 16, 18, 1, 13, 12, 7, 11]

def getCustomKey(s):
    """
    Parameters
    ----------
    s : is an input String containing the custom key of reflector in form - EJMZ....

    Returns : a list containing reflected integers on their respective indexed position
                example - [4,9,12,25 ....]
    """
    rk = []
    for ele in s:
        rk.append(ord(ele.upper())-65)    
    return rk    

class reflector(object ):
    
    def __init__(self , keyset = None ):
        """
        Parameters
        ----------
        keyset : is a string of set choosen for encryption.The default is None.

        """
        #if keyset not given ie Custom key case
        if keyset == None: 
            ReflectorKey = getCustomKey(s)
        # for setA = EJMZALYXVBWFCRQUONTSPIKHGD    
        elif keyset.upper() == 'REFLECTOR_A':
            self.wiring = Reflector_A
        # for setB = YRUHQSLDPXNGOKMIEBFZCWVJAT
        elif keyset.upper() == 'REFLECTOR_B':
            self.wiring = Reflector_B
        #for setC = FVPJIAOYEDRZXWGCTKUQSBNMHL
        elif keyset.upper() == 'REFLECTOR_C':
            self.wiring = Reflector_C

        else:
            raise ValueError ("Error: KeySet value should be - (A,B,C,None) only")
        
        self.ReflectorKey = ReflectorKey
                
        
    def ReflectorOut(self,R_in):
        """
        Parameters
        ----------
        Rin : is an integer. assume 0 <= Rin <26

        Returns : the reflected value of Rin in ReflectorKey
        """
        assert (R_in>=0 and R_in<26) , 'Error: Rin should between 0 and 26 only'
        return self.wiring[R_in]