"""
Utility functions for the Tagalog number converter.
"""

def validate_number(number):
    """
    Validates the input number for conversion.
    
    Args:
        number: The input to validate
        
    Returns:
        str: "valid" if valid, otherwise an error message
    """
    if not isinstance(number, int):
        return "Input must be an integer."
    if number < 0:
        return "Negative numbers are not supported."
    if number > 10**12 - 1:  # Up to trillions
        return "Numbers above 999,999,999,999 are not supported."
    return "valid"