#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

class Challenge(object):
    def __init__(self):
        self.score = 0
    
    def exercise_char_to_num(self, set_length=1):
        pass

    def exercise_num_to_char(self, set_length=1):
        pass
    
    def make_random_number(self, length):
        number = []
        for i in range(length):
            number.append(str(random.randint(0,9)))
        return "".join(number)

    def make_random_string(self, length):
        pass

class CharacterMapping(object):
    def __init__(self):
        self.language_ISO6392  = 'est'
        self.character_mapping = {
            u'n': '0',
            u'l': '1',
            u'k': '2',
            u'g': '2',
            u'q': '2',
            u'm': '3',
            u't': '4',
            u'v': '5',
            u'f': '5',
            u'w': '5',
            u'p': '6',
            u'b': '6',
            u's': '7',
            u'š': '7',
            u'ž': '7',
            u'z': '7',
            u'r': '8',
            u'j': '9',
            u'd': '9',
            u'h': '9',
        }

    def character_to_digit(self, character):
        if character.lower() in self.character_mapping.keys():
            return self.character_mapping[character.lower()]
        else:
            return ''

    def string_to_digits(self, string):
        """Converts a string of arbitrary length to string of digits
        
        Arguments:
            string {str} -- String you would like to transform to a string of digits
        
        Returns:
            str -- String of digits mapped from characters
        """

        return ''.join([self.character_to_digit(character) for character in string])
