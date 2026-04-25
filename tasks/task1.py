from datetime import datetime


def get_days_from_today(date: str) -> int:
    """
    Calculate the number of days between a given date and today.

    Args:
        date: A string representing a date in the format 'YYYY-MM-DD'.

    Throws:
        TypeError: If the date is not a string.
        ValueError: If the date is not in the format 'YYYY-MM-DD'.

    Returns:
        An integer representing the number of days between the given date and today.
    """
    if not isinstance(date, str):
        raise TypeError
    # Parse date or raise ValueError
    parsed_date = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.today()    
    return (today - parsed_date).days
