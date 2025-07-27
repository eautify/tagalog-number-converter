# tagalog-number-converter

A Python package for converting numerical digits to their Tagalog (Filipino) word representations.

## Features

- Converts integers (0 to trillions) to their Tagalog word equivalents
- Properly handles:
  - Number grouping (units, thousands, millions, etc.)
  - Ligatures ("-na" for numbers ending with vowels)
  - Conjunctions ("at" for decimal portions)
- Input validation to ensure only valid numbers are processed

## Installation

```bash
pip install tagalog-number
```

## Usage

### Basic Conversion

```python
from tagalog_number import tagalog_number

print(tagalog_number(123))  # "isang daan at dalawampu't tatlo"
print(tagalog_number(4567))  # "apat na libo't limang daan at animnapu't pito"
```

### Advanced Usage

```python
# Large numbers
print(tagalog_number(1000000))  # "isang milyon"

# Negative numbers
print(tagalog_number(-42))  # "minus apatnapu't dalawa"
```

## API Reference

### `tagalog_number(number: int) -> str`

Converts an integer to its Tagalog word representation.

**Parameters:**
- `number`: Integer to convert (supports numbers from -∞ to +∞)

**Returns:**
- String representation of the number in Tagalog

**Raises:**
- `TypeError`: If input is not an integer
- `ValueError`: If number is too large (trillions+) for accurate conversion

## Development

### Running Tests

```bash
python -m unittest discover tests
```

### Building the Package

```bash
python setup.py sdist bdist_wheel
```

## Contributing

Pull requests are welcome! Please ensure:

1. All tests pass
2. New features include appropriate tests
3. Follow existing code style

## License

MIT - See [LICENSE](LICENSE) for details.

## Author

Brian Lobrigas Balili - brian.balii3@gmail.com - https://github.com/eautify