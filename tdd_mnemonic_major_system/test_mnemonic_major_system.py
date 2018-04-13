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


