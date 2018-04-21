#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

class Challenge(object):
    def __init__(self, set_size=None, number_length=None, string_length=None, score=0):
        self.set_size = set_size
        self.number_length = number_length
        self.string_length = string_length
        self.score = score
    
    def exercise_char_to_num(self, set_length=1):
        pass

    def exercise_num_to_char(self):
        set_iter = self.make_random_number_sets()
        map = CharacterMapping()

        print('Map the following numbers to characters')
        for number in set_iter:
            user_input = input('{} ==> '.format(number))
            feedback = map.verify_match(number, user_input, num_to_char_task=True)
            print('Feedback: {}'.format(feedback))
            self.score += feedback.count(True)
        
        # TODO - exercise doesn't know the set size and number length to calculate 
        #        the potential maximum number of points.
        print('You final score: {}'.format(self.score))

    
    def make_random_number_sets(self, number_length=2, set_size=1):
        if self.number_length != None:
            number_length = self.number_length
        if self.set_size != None:
            set_size = self.set_size

        for set_i in range(set_size):
            number = []
            for i in range(number_length):
                number.append(str(random.randint(0,9)))
            yield "".join(number)

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
        """Returns a string of digits mapped from a given string"""
        return ''.join([self.character_to_digit(character) for character in string])

    def verify_match(self, task_string, user_input, num_to_char_task):
        # Given 13, expected lm
        correct = []
        if num_to_char_task:
            input_mapped_to_number = list(self.string_to_digits(user_input))
            task_string = list(task_string)
            error_potential = min(len(task_string), len(input_mapped_to_number))
            error_certain = max(len(task_string), len(input_mapped_to_number)) - error_potential
            while error_potential > 0:
                correct.append(task_string.pop(0) == input_mapped_to_number.pop(0))
                error_potential -= 1
        # Given lm, expected 13
        else:
            task_mapped_to_chars = list(self.string_to_digits(task_string))
            user_input = list(user_input)
            error_potential = min(len(task_mapped_to_chars), len(user_input))
            error_certain = max(len(task_mapped_to_chars), len(user_input)) - error_potential
            while error_potential > 0:
                correct.append(task_mapped_to_chars.pop(0) == user_input.pop(0))
                error_potential -= 1
        correct = correct + [False]*error_certain
        return correct

def main():
    map = Challenge(set_size=5)
    map.exercise_num_to_char()

if __name__ == '__main__':
    main()