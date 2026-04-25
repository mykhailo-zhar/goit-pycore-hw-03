import pytest

from tasks.task2 import get_numbers_ticket
import random

# Invalid input types

def test_invalid_input_types_returns_empty_list():
    assert get_numbers_ticket('nan', 'nan', 'nan') == []
    assert get_numbers_ticket('nan', 1, 1) == []
    assert get_numbers_ticket(1, 'nan', 1) == []
    assert get_numbers_ticket(1, 1, 'nan') == []

# Validation of input parameters

def test_min_out_of_range_returns_empty_list():
    assert get_numbers_ticket(-100, 10, 5) == []
    assert get_numbers_ticket(0, 10, 5) == []

def test_max_out_of_range_returns_empty_list():
    assert get_numbers_ticket(1, -100, 5) == []
    assert get_numbers_ticket(1, 0, 5) == []
    assert get_numbers_ticket(1, 1000, 5) == []

def test_min_greater_than_max_returns_empty_list():
    assert get_numbers_ticket(10, 1, 5) == []

def test_max_equals_min_returns_list_with_single_element():
    assert get_numbers_ticket(10, 10, 5) == [10]

def test_max_less_than_min_returns_empty_list():
    assert get_numbers_ticket(10, 1, 5) == []

def test_quantity_out_of_range_returns_empty_list():
    assert get_numbers_ticket(1, 10, -10) == []
    assert get_numbers_ticket(1, 10, 0) == []

# Validation of output parameters

def test_output_is_list():
    min, max, quantity = random.randint(-100, 100), \
                         random.randint(-100, 100), \
                         random.randint(-100, 100)
    assert isinstance(get_numbers_ticket(min, max, quantity), list)

# Logic

def test_quantity_greater_or_equals_returns_list_with_all_elements():
   assert len(get_numbers_ticket(1, 10, 10)) == 10
   assert len(get_numbers_ticket(1, 10, 100)) == 10

def test_quantity_less_than_returns_list_with_fewer_elements():
    assert len(get_numbers_ticket(1, 10, 5)) == 5
    assert len(get_numbers_ticket(1, 10, 1)) == 1

# Uniqueness of output values

def test_output_values_are_unique():
    assert len(set(get_numbers_ticket(1, 10, 5))) == 5

# Sortedness of output values

def test_output_values_are_sorted():
    result = get_numbers_ticket(1, 10, 5)
    assert sorted(result) == result