
import pytest
from datetime import datetime, timedelta
import random   
from tasks.task1 import get_days_from_today

def get_date_str_with_offset(offset: int) -> str:
    return (datetime.now() + timedelta(days=offset)).strftime("%Y-%m-%d")

def test_valid_date_string_returns_int():
    result = get_days_from_today("2000-01-01")
    assert type(result) is int


def test_non_string_input_raises_type_error():
    with pytest.raises(TypeError):
        get_days_from_today(2020)


def test_invalid_date_string_format_raises_value_error():
    with pytest.raises(ValueError):
        get_days_from_today("09-10-2021")


def test_prior_to_today_returns_positive():
    offset = random.randint(-100, -1)
    date_str = get_date_str_with_offset(offset)
    assert get_days_from_today(date_str) == -offset

def test_today_returns_zero():
    date_str = get_date_str_with_offset(0)
    assert get_days_from_today(date_str) == 0

def test_after_today_returns_negative():
    offset = random.randint(1, 100)
    date_str = get_date_str_with_offset(offset)
    assert get_days_from_today(date_str) == -offset