#? Explaining the base parameter in the int() function
from termcolor import cprint

#* Basic Usage of the base Parameter
# The int() function can convert a string representation of a number in a given base to an integer.
cprint("Basic Usage of the base Parameter", 'cyan')
binary_str = "101010"
octal_str = "52"
hex_str = "2A"

cprint(f"int('{binary_str}', 2): {int(binary_str, 2)}", 'green')  # Output: int('101010', 2): 42
cprint(f"int('{octal_str}', 8): {int(octal_str, 8)}", 'green')  # Output: int('52', 8): 42
cprint(f"int('{hex_str}', 16): {int(hex_str, 16)}", 'green')  # Output: int('2A', 16): 42

cprint('-'.center(40, '-'), 'magenta')

#* Converting from Different Bases
# You can convert strings from various bases (binary, octal, hexadecimal) to decimal integers.
cprint("Converting from Different Bases", 'cyan')
binary = 0b101010  # Binary representation
octal = 0o52       # Octal representation
hexadecimal = 0x2A # Hexadecimal representation

base_2_str = "1101"
base_8_str = "15"
base_16_str = "1F"

cprint(f"Binary to Decimal: int('{base_2_str}', 2): {int(base_2_str, 2)}", 'green')  # Output: Binary to Decimal: int('1101', 2): 13
cprint(f"Octal to Decimal: int('{base_8_str}', 8): {int(base_8_str, 8)}", 'green')  # Output: Octal to Decimal: int('15', 8): 13
cprint(f"Hexadecimal to Decimal: int('{base_16_str}', 16): {int(base_16_str, 16)}", 'green')  # Output: Hexadecimal to Decimal: int('1F', 16): 31

cprint('-'.center(40, '-'), 'magenta')

#* Invalid Conversions
# If the string contains characters not valid in the specified base, it raises a ValueError.
cprint("Invalid Conversions", 'cyan')
invalid_str = "1G"  # 'G' is not a valid hexadecimal character
try:
    cprint(f"Attempting invalid conversion: int('{invalid_str}', 16)", 'cyan')
    result = int(invalid_str, 16)
except ValueError as e:
    cprint(f"ValueError: {e}", 'red')  # Output: ValueError: invalid literal for int() with base 16: '1G'

cprint('-'.center(40, '-'), 'magenta')

#* Converting from Custom Bases
# You can specify any base from 2 to 36. The characters used are 0-9 and A-Z.
cprint("Converting from Custom Bases", 'cyan')
base_36_str = "Z"
cprint(f"Base-36 to Decimal: int('{base_36_str}', 36): {int(base_36_str, 36)}", 'green')  # Output: Base-36 to Decimal: int('Z', 36): 35

cprint('-'.center(40, '-'), 'magenta')

#* Real-world Example
# Converting user input from different bases to decimal.
cprint("Real-world Example", 'cyan')
user_input = "1010"
base = 2
converted_value = int(user_input, base)
cprint(f"User input '{user_input}' in base {base} is {converted_value} in decimal.", 'green')  # Output: User input '1010' in base 2 is 10 in decimal.

# This is a comprehensive overview of the base parameter in the int() function and its usage in Python.