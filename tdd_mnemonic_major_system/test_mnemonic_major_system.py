#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from . import mnemonic_major_system as mnemo

@pytest.fixture
def map():
    return mnemo.CharacterMapping()

@pytest.mark.parametrize('character,expected', [
    (u'n', '0'), (u'l', '1'), (u'k', '2'), (u'g', '2'),
    (u'm', '3'), (u't', '4'), (u'v', '5'), (u'f', '5'),
    (u'w', '5'), (u'p', '6'), (u'b', '6'), (u's', '7'),
    (u'š', '7'), (u'z', '7'), (u'ž', '7'), (u'r', '8'),
    (u'j', '9'), (u'd', '9'), (u'h', '9')
    ])
def test_character_to_digit_conversion_lowercase(map, character, expected):
    assert map.character_to_digit(character) == expected

@pytest.mark.parametrize('character,expected', [
    (u'N', '0'), (u'L', '1'), (u'K', '2'), (u'G', '2'),
    (u'M', '3'), (u'T', '4'), (u'V', '5'), (u'F', '5'),
    (u'W', '5'), (u'P', '6'), (u'B', '6'), (u'S', '7'),
    (u'Š', '7'), (u'Z', '7'), (u'Ž', '7'), (u'R', '8'),
    (u'J', '9'), (u'D', '9'), (u'H', '9')
    ])
def test_character_to_digit_conversion_uppercase(map, character, expected):
    assert map.character_to_digit(character) == expected

@pytest.mark.parametrize('character,expected', [
    (u'a', ''), (u'e', ''), (u'i', ''), (u'o', ''),
    (u'u', ''), (u'õ', ''), (u'ä', ''), (u'ö', ''),
    (u'ü', '')
    ])
def test_character_to_digit_conversion_vocals(map, character, expected):
    assert map.character_to_digit(character) == expected

@pytest.mark.parametrize('string,expected', [
    (u'luuk', '12'), (u'mõõk', '32'),
    (u'tool', '41'), (u'vaip', '56'),
    (u'puus', '67'), (u'osuti', '74'),
    (u'rauk', '82'), (u'raud', '89'),
    (u'haud', '99'), (u'hani', '90'),
    (u'KARU', '28'), (u'John Doe', '9909')
    ])
def test_string_to_digits_conversion_vocals(map, string, expected):
    assert map.string_to_digits(string) == expected

@pytest.mark.parametrize('task_string,user_input,expected', [
    #('','' ,[]),('a','',['a']),('a','a' ,None), # Task should not be empty
    ('1','l',[True]),
    ('3','k',[False]),  # Mismapping is error
    ('4','',[False]),   # Error for every number not mapped
    ('2','kg',[True,False]),    # Number should be mapped to one of the options
    ('2','gk',[True,False]),    # Number should be mapped to one of the options
    ('1','ll',[True,False]),    # Additions are errors
    ('1','kk',[False,False]),   # Mismapping and addition
    ('1','kl',[False,False]),   # Shift is an error

    ('12','',[False,False]),    # Error for every number not mapped
    ('12','l',[True,False]),    # Error for every number not mapped
    ('21','l',[False,False]),   # Shift is an error
    ('22','kg',[True,True]),
    ('12','lkm',[True,True,False]),     # Additions are errors
    ('12','mlk',[False,False,False]),   # Shift is a full error

    ('322','',[False,False,False]), # Error for every number not mapped
    ('322','mmm' ,[True,False,False]),
    ('223','mmm' ,[False,False,True]),
    ('123','lkm',[True,True,True]),
    ('123','lgm',[True,True,True]),
    ('123','lkgm',[True,True,False,False]),

    ('2','mprkvmptmg',[False,False,False,False,False,False,False,False,False,False]),
    ])
def test_verify_match_num_to_char_task(map, task_string, user_input, expected):
    assert map.verify_match(task_string, user_input, num_to_char_task=True) == expected

@pytest.mark.parametrize('task_string,user_input,expected', [
    #('','' ,[]),('a','',['a']),('a','a' ,None), # Task should not be empty
    ('l','1',[True]),
    ('k','3',[False]),  # Mismapping is error
    ('l','',[False]),   # Error for every task item not mapped
    ('k','22',[True,False]),    # Character should be mapped to one number
    ('g','22',[True,False]),    # Character should be mapped to one number
    ('l','11',[True,False]),    # Additions are errors
    ('l','21',[False,False]),    # Shift and additions are errors

    ('kg','22',[True,True]),
    ('lk','1',[True,False]),    # Error for every item not mapped
    ('kk','1',[False,False]),   # Mismapping and missing an item
    ('kl','1',[False,False]),   # Shift is an error
    ('lk','',[False,False]),    # Error for every item not mapped
    ('mm','333',[True,True, False]),    # Additions are errors
    ('lk','123',[True,True,False]),     # Additions are errors
    ('lk','312',[False,False,False]),   # Shift is a full error

    ('lkm','123',[True,True,True]),
    ('lgm','123',[True,True,True]),
    ('lkm','',[False,False,False]), # Error for every number not mapped
    ('kmm','222' ,[True,False,False]),
    ('mmk','222' ,[False,False,True]),
    ('lkm','1223',[True,True,False,False]),

    ('l','0123456789',[False,False,False,False,False,False,False,False,False,False]),
    ('mprkvmptmg','',[False,False,False,False,False,False,False,False,False,False]),
    ])
def test_verify_match_char_to_num_task(map, task_string, user_input, expected):
    assert map.verify_match(task_string, user_input, num_to_char_task=False) == expected

# TODO
# * When user input is alphanum