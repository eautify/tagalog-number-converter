from .utils import validate_number

def tagalog_number(number):
    """
    Translates English numbers (integers) to Tagalog worded numbers,
    correcting grammatical usage of 'at', 'daan'/'raan', and ligatures for larger numbers.

    Args:
        number (int): The English number to translate. Supports up to billions.

    Returns:
        str: The Tagalog worded number, or an error message if the number is out of scope.
    """

    if not isinstance(number, int):
        return "Input must be an integer."
    if number < 0:
        return "Negative numbers are not supported."

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

    # Helper function to apply 'ng' or 'na' ligature to a number phrase
    def apply_ligature_and_determine_hundred(num_phrase, is_prefix_for_hundred=False):
        if not num_phrase:
            return "", "daan" # Default to daan if no number word

        # The ligature rule is based on the *last word* of the number phrase.
        last_word = num_phrase.split()[-1]

        # Determine ligature
        use_ng = False
        # Special cases for 'isa' when it becomes 'isang'
        if num_phrase == "isa" and is_prefix_for_hundred:
            return "isang", "daan"
        
        # General ligature rules
        if last_word.endswith(('a', 'e', 'i', 'o', 'u', 'w', 'y')): # Vowel or 'w'/'y' ending usually takes 'ng'
            use_ng = True
        elif last_word == "sampu": # Explicitly 'sampu' takes 'ng'
            use_ng = True
        elif last_word in ["dalawampu", "tatlumpu", "limampu", "pitumpu", "walumpu", "siyamnapu"]: # Tens ending in 'pu' take 'ng'
             use_ng = True
        # For 'labing-' forms, the ligature depends on the root, but for our purpose,
        # if the whole 'labing-' word is the last_word, it already contains the 'ng'.
        # We need to consider the root for further ligatures, but here we're checking the last word.
        # This function is primarily for ligatures *before* daan/libo/milyon/bilyon.

        ligatured_phrase = f"{num_phrase}ng" if use_ng else f"{num_phrase} na"
        
        # Determine 'daan' or 'raan' based on the ligature determined
        # If 'ng' is used, it takes 'd' (daan). If 'na' is used, it takes 'r' (raan).
        hundred_word = "daan" if use_ng or num_phrase == "isa" else "raan"
        
        return ligatured_phrase, hundred_word

    # Function to convert numbers from 1 to 999
    def convert_hundreds_block(n):
        if n == 0:
            return ""

        parts = []
        original_n = n # Store original value to check if hundreds were present

        # Hundreds (100-999)
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

        # Tens and Units (0-99)
        if n > 0:
            current_sub_part = ""
            if 1 <= n <= 10:
                current_sub_part = basic_numerals[n]
            elif 11 <= n <= 19:
                unit = n % 10
                unit_word = basic_numerals[unit]
                # Specific rules for labing-
                if unit_word[0] in 'aeiou': # e.g., labing-isa, labing-apat
                    current_sub_part = f"labing-{unit_word}"
                elif unit_word[0] == 'o': # e.g., labing-walo
                    current_sub_part = f"labing-{unit_word}" # 'w' is sometimes treated as a vowel for ligatures
                elif unit_word[0] in 'dt': # e.g., labin-dalawa, labin-tatlo
                    current_sub_part = f"labin{unit_word}"
                elif unit_word[0] == 'p': # e.g., labim-pito
                    current_sub_part = f"labim{unit_word}"
                else: # Fallback
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
                    # Use 'at' for 21-99 where it's tens_word at unit_word
                    current_sub_part = f"{tens_word}'t {basic_numerals[unit_digit]}"
            
            # Connect hundreds to tens/units with 'at' or 't
            if original_n >= 100 and n > 0: # If there was a hundreds part and a remainder
                 parts.append("at") # Add 'at' after the hundreds part
            
            # Then add the tens/units
            parts.append(current_sub_part)
            
        return " ".join(filter(None, parts)).strip() # Use filter(None, parts) to remove empty strings

    final_output_parts = []
    
    # Billions
    if number >= 1_000_000_000:
        billion_val = number // 1_000_000_000
        billion_phrase = convert_hundreds_block(billion_val)
        if billion_phrase:
            # Ligature for billion_phrase before "bilyon"
            ligatured_billion_phrase, _ = apply_ligature_and_determine_hundred(billion_phrase)
            final_output_parts.append(f"{ligatured_billion_phrase} bilyon")
        number %= 1_000_000_000

    # Millions
    if number >= 1_000_000:
        million_val = number // 1_000_000
        million_phrase = convert_hundreds_block(million_val)
        if million_phrase:
            # Add 'at' if a previous block (billions) exists and there's a remainder
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
            # Add 'at' if a previous block (billions/millions) exists and there's a remainder
            if final_output_parts and (number > 0 or (number == 0 and (billion_val > 0 or million_val > 0))):
                final_output_parts.append("at") 
            ligatured_thousand_phrase, _ = apply_ligature_and_determine_hundred(thousand_phrase)
            final_output_parts.append(f"{ligatured_thousand_phrase} libo")
        number %= 1_000

    # Remaining hundreds, tens, and units
    if number > 0:
        remaining_phrase = convert_hundreds_block(number)
        if remaining_phrase:
            # Add 'at' if there were any preceding larger magnitude blocks
            if final_output_parts:
                final_output_parts.append("at")
            final_output_parts.append(remaining_phrase)

    return " ".join(final_output_parts).strip()

