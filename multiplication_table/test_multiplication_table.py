#!/usr/bin/env python3

import multiplication_table
from multiplication_table import NotPositiveDimensionsException, TooBigDimensionsException
import pytest

@pytest.fixture
def table_5x5():
    '''Returns an empty MultiplicationTable'''
    return multiplication_table.MultiplicationTable(5,5)

def test_negative_dimensions():
    with pytest.raises(NotPositiveDimensionsException):
        multiplication_table.MultiplicationTable(-1,3)

def test_zero_zero_dimensions():
    with pytest.raises(NotPositiveDimensionsException):
        multiplication_table.MultiplicationTable(0,0)

def test_too_big_dimensions():
    ok_dimension = multiplication_table.DIMENSION_MAX
    too_big_dimension = multiplication_table.DIMENSION_MAX+1
    with pytest.raises(TooBigDimensionsException):
        multiplication_table.MultiplicationTable(too_big_dimension, too_big_dimension)
        multiplication_table.MultiplicationTable(too_big_dimension, ok_dimension)
        multiplication_table.MultiplicationTable(ok_dimension, too_big_dimension)

def test_correct_number_of_rows(table_5x5):
    rows = table_5x5.show_table_string().strip("\n").split("\n")
    assert len(rows) == 5

def test_correct_number_of_columns(table_5x5):
    rows = table_5x5.show_table_string().strip("\n").split("\n")
    for row in rows:
        columns = row.strip().split()
        assert len(columns) == 5

def test_first_element_not_zero(table_5x5):
    first_row = table_5x5.show_table_string().split("\n")[0]
    first_element = first_row.split()[0]
    assert int(first_element) != 0
