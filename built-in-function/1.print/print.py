import time

for i in range(5):
    print(i, end=' ', flush=True)
    time.sleep(0.1)

for i in range(20):
    print(f'\rProgreso: {i}%', end=' ', flush=True)
    time.sleep(0.1)


#? Explaining the print() function and its arguments
from termcolor import cprint

#* Basic Usage
# The print() function prints the specified message to the screen.
message = "Hello, World!"
cprint("Basic Usage", 'cyan')
cprint(message, 'green')
print(message)  # Output: Hello, World!

cprint('-'.center(40, '-'), 'magenta')

#* sep Argument
# The sep parameter specifies a separator between the objects to be printed.
cprint("Using sep Argument", 'cyan')
print("Python", "is", "awesome", sep="-")  # Output: Python-is-awesome

cprint('-'.center(40, '-'), 'magenta')

#* end Argument
# The end parameter specifies what to print at the end. Default is '\n' (newline).
cprint("Using end Argument", 'cyan')
print("Hello", end=" ")
print("World!")  # Output: Hello World!

cprint('-'.center(40, '-'), 'magenta')

#* file Argument
# The file parameter specifies the file or stream to print to. Default is sys.stdout.
import sys
cprint("Using file Argument", 'cyan')
print("This is a message", file=sys.stdout)  # Output: This is a message

cprint('-'.center(40, '-'), 'magenta')

#* flush Argument
# The flush parameter specifies whether to flush the output buffer. Default is False.
cprint("Using flush Argument", 'cyan')
print("This is a message", flush=True)  # Output: This is a message

cprint('-'.center(40, '-'), 'magenta')

#* Combining Arguments
# You can combine these arguments to customize the output.
cprint("Combining Arguments", 'cyan')
print("Hello", "World", sep=", ", end="!!!\n", file=sys.stdout, flush=True)  # Output: Hello, World!!!

cprint('-'.center(40, '-'), 'magenta')

#* Printing Different Data Types
# The print() function can handle multiple data types.
cprint("Printing Different Data Types", 'cyan')
print("String:", "Hello, World!")          # Output: String: Hello, World!
print("Integer:", 42)                      # Output: Integer: 42
print("Float:", 3.14159)                   # Output: Float: 3.14159
print("List:", [1, 2, 3])                  # Output: List: [1, 2, 3]

cprint('-'.center(40, '-'), 'magenta')

#* Printing Variables
# You can directly print variables and combine them with text.
cprint("Printing Variables", 'cyan')
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  # Output: My name is Alice and I am 30 years old.

cprint('-'.center(40, '-'), 'magenta')

#* Using Format Method
# You can use the format() method to format strings.
cprint("Using Format Method", 'cyan')
print("Hello, {}. You are {} years old.".format(name, age))  # Output: Hello, Alice. You are 30 years old.

cprint('-'.center(40, '-'), 'magenta')

#* Printing with Different Endings
# Demonstrating the use of different endings with the end parameter.
cprint("Printing with Different Endings", 'cyan')
print("This is the first line.", end=" ")
print("This is still the first line.")  # Output: This is the first line. This is still the first line.

cprint('-'.center(40, '-'), 'magenta')

#* Advanced Example with Multiple Arguments
# Combining sep, end, and flush in a single print statement.
cprint("Advanced Example with Multiple Arguments", 'cyan')
print("Advanced", "usage", sep="***", end="---\n", flush=True)  # Output: Advanced***usage---

# This is a comprehensive overview of the print() function and its arguments in Python.
