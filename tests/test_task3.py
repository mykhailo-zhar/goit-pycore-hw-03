import pytest

from tasks.task3 import normalize_phone_number


def test_non_string_input_raises_type_error():
    with pytest.raises(TypeError):
        normalize_phone_number(1234567890)


@pytest.mark.parametrize(
    "phone",
    [
        "".join(str(i) for i in range(1, 5)),
        "".join(str(i % 10) for i in range(1, 17)),
    ],
)
def test_invalid_phone_number_raises_value_error(phone):
    with pytest.raises(ValueError):
        normalize_phone_number(phone)


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
parsed_numbers = [
    "+380671234567",
    "+380952345678",
    "+380441234567",
    "+380501234567",
    "+380501233234",
    "+380503451234",
    "+380508889900",
    "+380501112222",
    "+380501112211",
]


@pytest.mark.parametrize("phone,normalized_phone", zip(raw_numbers, parsed_numbers))
def test_normalize_phone_number_valid_input(phone, normalized_phone):
    assert normalize_phone_number(phone) == normalized_phone
