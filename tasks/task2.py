from random import sample

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

    if not isinstance(min, int) \
        or not isinstance(max, int) \
        or not isinstance(quantity, int):
      return []
    
    if min < 1:
      return []
    
    if max >= 1000 or max < 1:
      return []
    
    if max < min:
      return []
    
    if quantity < 1:
      return []

    if quantity >= max - min + 1:
      return list(range(min, max + 1))

    samples = sample(range(min, max + 1), k=quantity)
    return sorted(samples[:quantity])