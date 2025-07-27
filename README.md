# Tagalog Number Converter

A Python package for converting between numbers and their Tagalog word representations, with proper grammatical handling of ligatures and number groupings.

## Features

- Convert numbers (0 to 999,999,999,999) to Tagalog words with proper grammar
- Supports conversion back from Tagalog words to digits
- Proper handling of:
  - Ligatures ("ng" and "na")
  - Number groupings (daan/raan for hundreds)
  - Special cases for teens (labing-isa, labindalawa, etc.)
  - Contractions ("libo't", "dalawampu't")

## Installation

```bash
pip install tagalog-number-converter
```

## Usage

```python
from tagalog_number import digits_to_tagalog_number, tagalog_number_to_digits

# Convert number to Tagalog words
print(digits_to_tagalog_number(123))  # "isang daan at dalawampu't tatlo"
print(digits_to_tagalog_number(4567)) # "apat na libo't limang daan at animnapu't pito"

# Convert Tagalog words back to number
print(tagalog_number_to_digits("isang daan at dalawampu't tatlo"))  # 123
print(tagalog_number_to_digits("apat na libo't limang daan"))       # 4500

# Input validation
from tagalog_number import validate_number
print(validate_number(1000000000000))  # "Numbers above 999,999,999,999 are not supported."
```

## Supported Number Range

- Numbers: 0 to 999,999,999,999 (up to trillions)
- Tagalog words: "sero" to "siyam na raan siyamnapu't siyam na bilyon..."

## Examples

| Number | Tagalog Representation |
|--------|------------------------|
| 0      | sero |
| 11     | labing-isa |
| 20     | dalawampu |
| 25     | dalawampu't lima |
| 100    | isang daan |
| 123    | isang daan at dalawampu't tatlo |
| 1000   | isang libo |
| 1234   | isang libo't dalawang daan at tatlumpu't apat |
| 1000000 | isang milyon |
| 1000000000 | isang bilyon |

## Limitations

- The reverse conversion (Tagalog words to digits) has limited functionality and may not handle all valid Tagalog number phrases
- Very large numbers (above trillions) are not supported

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

MIT - See [LICENSE](LICENSE) for details.