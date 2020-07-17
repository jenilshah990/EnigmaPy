#!/usr/bin/env python
#-*- coding: utf-8 -*-

class plugboard:
    # Wires the plugboard from the settings provided in wiring_pairs
    def __init__(self, wiring_pairs=None):
        # Creating a default 1:1 wiring
        self.wiring = list(range(26))
        if not wiring_pairs:
            return
        else:
            # Converts the writing_pairs in the form 'AJ RT PQ..' to '[(0,9), (16, 19)...] & then converts the wirings
            for p in wiring_pairs.upper().split():
                m = ord(p[0]) - ord('A')
                n = ord(p[1]) - ord('A')
                self.wiring[m] = n
                self.wiring[n] = m

    # The letter is encrypted according to the plugboard wiring
    def plugboard_encrypt(self, letter):
        letter_index = ord(letter.upper()) - ord('A')
        return self.wiring[letter_index]
