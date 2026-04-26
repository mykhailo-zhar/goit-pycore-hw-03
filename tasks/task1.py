from datetime import datetime


def get_days_from_today(date: str) -> int:
    """
    Calculate the number of days between a given date and today.

    Args:
        date: A string representing a date in the format 'YYYY-MM-DD'.

    Returns:
        An integer representing the number of days between the given date and today.
    """
    parsed_date = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.today()
    return (today - parsed_date).days
