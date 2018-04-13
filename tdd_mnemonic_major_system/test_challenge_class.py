#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest
from . import mnemonic_major_system as mnemo

@pytest.fixture
def basic_challenge():
    return mnemo.Challenge()

@pytest.mark.parametrize('length', [
    -1, 0, 1, 10
    ])
def test_make_random_number_length(basic_challenge, length):
    number = basic_challenge.make_random_number(length=length)
    assert len(number) == length or ((length < 0) and len(number) == 0)