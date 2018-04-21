#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from . import mnemonic_major_system as mnemo

@pytest.fixture
def basic_challenge():
    return mnemo.Challenge()

@pytest.mark.parametrize('number_length', [
    -1, 0, 1, 10
    ])
def test_make_random_number_sets_number_length(basic_challenge, number_length):
    number = basic_challenge.make_random_number_sets(number_length=number_length).next()
    assert len(number) == number_length or ((number_length < 0) and len(number) == 0)

@pytest.mark.parametrize('set_size', [
    -1, 0, 1, 10
    ])
def test_make_random_number_sets_length(basic_challenge, set_size):
    set_iter = basic_challenge.make_random_number_sets(set_size=set_size)
    set_size_returned = 0
    for number in set_iter:
        set_size_returned += 1
    
    assert set_size == set_size_returned or (set_size < 0 and set_size_returned == 0)

@pytest.mark.parametrize('set_size', [
    -1, 0, 1, 10
    ])
def test_exercise_num_to_char_scoring(basic_challenge, set_size):
    # Test not written
    pass