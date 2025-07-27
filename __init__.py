"""Tagalog Number Converter - A package to convert numbers to Tagalog words."""
from .converter import tagalog_number, tagalog_number_to_digits
from .utils import validate_number

__version__ = "1.0.0"
__all__ = ['tagalog_number', 'tagalog_number_to_digits', 'validate_number']