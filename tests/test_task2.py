import random

import pytest

from tasks.task2 import get_numbers_ticket

# Invalid input types


@pytest.mark.parametrize(
    "minimum,maximum,quantity",
    [
        ("nan", "nan", "nan"),
        ("nan", 1, 1),
        (1, "nan", 1),
        (1, 1, "nan"),
    ],
)
def test_invalid_input_types_returns_empty_list(minimum, maximum, quantity):
    assert get_numbers_ticket(minimum, maximum, quantity) == []


@pytest.mark.parametrize(
    "minimum,maximum,quantity",
    [
        (-100, 10, 5),
        (0, 10, 5),
    ],
)
def test_minimum_out_of_range_returns_empty_list(minimum, maximum, quantity):
    assert get_numbers_ticket(minimum, maximum, quantity) == []


@pytest.mark.parametrize(
    "minimum,maximum,quantity",
    [
        (1, -100, 5),
        (1, 0, 5),
        (1, 1000, 5),
    ],
)
def test_maximum_out_of_range_returns_empty_list(minimum, maximum, quantity):
    assert get_numbers_ticket(minimum, maximum, quantity) == []


def test_minimum_greater_than_maximum_returns_empty_list():
    assert get_numbers_ticket(10, 1, 5) == []


def test_maximum_equals_minimum_returns_list_with_single_element():
    assert get_numbers_ticket(10, 10, 5) == [10]


def test_maximum_less_than_minimum_returns_empty_list():
    assert get_numbers_ticket(10, 1, 5) == []


@pytest.mark.parametrize(
    "minimum,maximum,quantity",
    [
        (1, 10, -10),
        (1, 10, 0),
    ],
)
def test_quantity_out_of_range_returns_empty_list(minimum, maximum, quantity):
    assert get_numbers_ticket(minimum, maximum, quantity) == []


# Validation of output parameters


def test_output_is_list():
    minimum, maximum, quantity = (
        random.randint(-100, 100),
        random.randint(-100, 100),
        random.randint(-100, 100),
    )
    assert isinstance(get_numbers_ticket(minimum, maximum, quantity), list)


# Logic


@pytest.mark.parametrize(
    "minimum,maximum,quantity",
    [
        (1, 10, 10),
        (1, 10, 100),
    ],
)
def test_quantity_greater_or_equals_returns_list_with_all_elements(
    minimum, maximum, quantity
):
    assert len(get_numbers_ticket(minimum, maximum, quantity)) == min(maximum, quantity)


@pytest.mark.parametrize(
    "minimum,maximum,quantity ",
    [
        (1, 10, 5),
        (1, 10, 1),
    ],
)
def test_quantity_less_than_returns_list_with_fewer_elements(
    minimum, maximum, quantity
):
    assert len(get_numbers_ticket(minimum, maximum, quantity)) == quantity


# Uniqueness of output values


def test_output_values_are_unique():
    assert len(set(get_numbers_ticket(1, 100, 50))) == 50


# Sortedness of output values


def test_output_values_are_sorted():
    result = get_numbers_ticket(1, 10, 5)
    assert sorted(result) == result
