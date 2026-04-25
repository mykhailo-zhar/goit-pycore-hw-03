import re

def _convert_to_digits(phone: str) -> str:
    return re.sub(r'\D', '', phone)

def _convert_to_international(phone: str, country_code: str) -> str:
    if phone.startswith('0') or not phone.startswith(country_code):
      return f"{country_code}{phone}"

    return phone

def normalize_phone_number(phone: str, country_code: str = '38') -> str:
    """
    Normalize a phone number.

    Args:
        phone: The phone number to normalize.
    """
    if not isinstance(phone, str):
        raise TypeError(f"Phone must be a string, got {type(phone)}")
    
    phone_digits = _convert_to_digits(phone)
    phone_digits = _convert_to_international(phone_digits, country_code)
    if len(phone_digits) < 12 or len(phone_digits) > 15:
        raise ValueError(f"Phone must be between 12 and 15 digits, got {len(phone_digits)}")
    
    return f"+{phone_digits}"