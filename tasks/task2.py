from random import sample


def _validate_input(min: int, max: int, quantity: int) -> bool:
    """
    Validate the input parameters.

    Args:
        min: The minimum possible number in the range.
        max: The maximum possible number in the range.
        quantity: The number of numbers to generate.
    """
    is_valid = True

    is_valid &= isinstance(min, int)
    is_valid &= isinstance(max, int)
    is_valid &= isinstance(quantity, int)

    if not is_valid:
      return is_valid
    
    is_valid &= min >= 1
    is_valid &= max >= 1
    is_valid &= max < 1000
    is_valid &= max >= min
    is_valid &= quantity >= 1

    return is_valid


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    Generate a list of unique random numbers within a given range.

    Args:
        min: The minimum possible number in the range.
        max: The maximum possible number in the range.
        quantity: The number of numbers to generate.

    Returns:
        A list of unique random numbers within the given range.
    """


    if not _validate_input(min, max, quantity):
      return []
    
    if quantity >= max - min + 1:
      return list(range(min, max + 1))

    samples = sample(range(min, max + 1), k=quantity)
    return sorted(samples[:quantity])