"""
Main module for converting between numbers and Tagalog words.
"""

from .utils import validate_number

def tagalog_number(number):
    """
    Translates English numbers (integers) to Tagalog worded numbers,
    correcting grammatical usage of 'at', 'daan/'raan', and ligatures for larger numbers.

    Args:
        number (int): The English number to translate. Supports up to billions.

    Returns:
        str: The Tagalog worded number, or an error message if the number is out of scope.

    Examples:
        >>> tagalog_number(123)
        "isang daan at dalawampu't tatlo"
        >>> tagalog_number(4567)
        "apat na libo't limang daan at animnapu't pito"
    """
    validation_result = validate_number(number)
    if validation_result != "valid":
        return validation_result

    if number == 0:
        return "sero"

    basic_numerals = {
        0: "",
        1: "isa",
        2: "dalawa",
        3: "tatlo",
        4: "apat",
        5: "lima",
        6: "anim",
        7: "pito",
        8: "walo",
        9: "siyam",
        10: "sampu"
    }

    def apply_ligature_and_determine_hundred(num_phrase, is_prefix_for_hundred=False):
        if not num_phrase:
            return "", "daan"

        last_word = num_phrase.split()[-1]

        use_ng = False
        if num_phrase == "isa" and is_prefix_for_hundred:
            return "isang", "daan"
        
        if last_word.endswith(('a', 'e', 'i', 'o', 'u', 'w', 'y')):
            use_ng = True
        elif last_word == "sampu":
            use_ng = True
        elif last_word in ["dalawampu", "tatlumpu", "limampu", "pitumpu", "walumpu", "siyamnapu"]:
             use_ng = True

        ligatured_phrase = f"{num_phrase}ng" if use_ng else f"{num_phrase} na"
        hundred_word = "daan" if use_ng or num_phrase == "isa" else "raan"
        
        return ligatured_phrase, hundred_word

    def convert_hundreds_block(n):
        if n == 0:
            return ""

        parts = []
        original_n = n

        if n >= 100:
            hundreds_val = n // 100
            remainder = n % 100
            
            if hundreds_val == 1:
                parts.append("isang daan")
            else:
                base_num_word = basic_numerals[hundreds_val]
                ligatured_prefix, hundred_form = apply_ligature_and_determine_hundred(base_num_word, is_prefix_for_hundred=True)
                parts.append(f"{ligatured_prefix} {hundred_form}")
            
            n = remainder

        if n > 0:
            current_sub_part = ""
            if 1 <= n <= 10:
                current_sub_part = basic_numerals[n]
            elif 11 <= n <= 19:
                unit = n % 10
                unit_word = basic_numerals[unit]
                if unit_word[0] in 'aeiou':
                    current_sub_part = f"labing-{unit_word}"
                elif unit_word[0] == 'o':
                    current_sub_part = f"labing-{unit_word}"
                elif unit_word[0] in 'dt':
                    current_sub_part = f"labin{unit_word}"
                elif unit_word[0] == 'p':
                    current_sub_part = f"labim{unit_word}"
                else:
                    current_sub_part = f"labing-{unit_word}"
            elif 20 <= n <= 99:
                tens_digit = n // 10
                unit_digit = n % 10

                tens_word = ""
                if tens_digit == 2:
                    tens_word = "dalawampu"
                elif tens_digit == 3:
                    tens_word = "tatlumpu"
                elif tens_digit == 4:
                    tens_word = "apatnapu"
                elif tens_digit == 5:
                    tens_word = "limampu"
                elif tens_digit == 6:
                    tens_word = "animnapu"
                elif tens_digit == 7:
                    tens_word = "pitumpu"
                elif tens_digit == 8:
                    tens_word = "walumpu"
                elif tens_digit == 9:
                    tens_word = "siyamnapu"
                
                if unit_digit == 0:
                    current_sub_part = tens_word
                else:
                    current_sub_part = f"{tens_word}'t {basic_numerals[unit_digit]}"
            
            if original_n >= 100 and n > 0:
                 parts.append("at")
            
            parts.append(current_sub_part)
            
        return " ".join(filter(None, parts)).strip()

    final_output_parts = []
    
    # Billions
    if number >= 1_000_000_000:
        billion_val = number // 1_000_000_000
        billion_phrase = convert_hundreds_block(billion_val)
        if billion_phrase:
            ligatured_billion_phrase, _ = apply_ligature_and_determine_hundred(billion_phrase)
            final_output_parts.append(f"{ligatured_billion_phrase} bilyon")
        number %= 1_000_000_000

    # Millions
    if number >= 1_000_000:
        million_val = number // 1_000_000
        million_phrase = convert_hundreds_block(million_val)
        if million_phrase:
            if final_output_parts and (number > 0 or (number == 0 and billion_val > 0)):
                final_output_parts.append("at")
            ligatured_million_phrase, _ = apply_ligature_and_determine_hundred(million_phrase)
            final_output_parts.append(f"{ligatured_million_phrase} milyon")
        number %= 1_000_000

    # Thousands
    if number >= 1_000:
        thousand_val = number // 1_000
        thousand_phrase = convert_hundreds_block(thousand_val)
        if thousand_phrase:
            if final_output_parts and (number > 0 or (number == 0 and (billion_val > 0 or million_val > 0))):
                final_output_parts.append("at") 
            ligatured_thousand_phrase, _ = apply_ligature_and_determine_hundred(thousand_phrase)
            final_output_parts.append(f"{ligatured_thousand_phrase} libo")
        number %= 1_000

    if number > 0:
        remaining_phrase = convert_hundreds_block(number)
        if remaining_phrase:
            if final_output_parts:
                final_output_parts.append("at")
            final_output_parts.append(remaining_phrase)

    return " ".join(final_output_parts).strip()

def tagalog_number_to_digits(tagalog_str):
    """
    Converts a Tagalog number phrase back to digits (limited functionality).
    
    Args:
        tagalog_str (str): The Tagalog number phrase to convert
        
    Returns:
        int: The converted number, or None if conversion fails
    """
    # This is a basic implementation - would need expansion for full functionality
    word_to_num = {
        'sero': 0,
        'isa': 1, 'isang': 1,
        'dalawa': 2, 'dalawang': 2,
        'tatlo': 3, 'tatlong': 3,
        'apat': 4, 'apat na': 4,
        'lima': 5, 'limang': 5,
        'anim': 6, 'anim na': 6,
        'pito': 7, 'pitong': 7,
        'walo': 8, 'walong': 8,
        'siyam': 9, 'siyam na': 9,
        'sampu': 10,
        'labing-isa': 11,
        'labindalawa': 12,
        'labintatlo': 13,
        'labing-apat': 14,
        'labinlima': 15,
        'labing-anim': 16,
        'labimpito': 17,
        'labingwalo': 18,
        'labinsiyam': 19,
        'dalawampu': 20,
        'tatlumpu': 30,
        'apatnapu': 40,
        'limampu': 50,
        'animnapu': 60,
        'pitumpu': 70,
        'walumpu': 80,
        'siyamnapu': 90,
        'daan': 100, 'raan': 100,
        'libo': 1000,
        'milyon': 1000000,
        'bilyon': 1000000000
    }
    
    try:
        parts = tagalog_str.replace("'t ", " at ").replace(" at ", " ").split()
        total = 0
        current = 0
        
        for word in parts:
            if word in ['daan', 'raan']:
                if current == 0:
                    current = 100
                else:
                    current *= 100
            elif word == 'libo':
                if current == 0:
                    current = 1000
                total += current * 1000
                current = 0
            elif word == 'milyon':
                if current == 0:
                    current = 1000000
                total += current * 1000000
                current = 0
            elif word == 'bilyon':
                if current == 0:
                    current = 1000000000
                total += current * 1000000000
                current = 0
            elif word in word_to_num:
                current += word_to_num[word]
        
        total += current
        return total
    except:
        return None