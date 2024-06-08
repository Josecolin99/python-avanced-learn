#? Explaining the type() function and its usage
from termcolor import cprint

#* Basic Usage
# The type() function returns the type of the specified object.
cprint("Basic Usage", 'cyan')
example_int = 42
example_str = "Hello, World!"
cprint(f"Type of {example_int}: {type(example_int)}", 'green')  # Output: <class 'int'>
cprint(f"Type of '{example_str}': {type(example_str)}", 'green')  # Output: <class 'str'>

cprint('-'.center(40, '-'), 'magenta')

#* Checking Types
# You can use type() to check the type of different objects.
cprint("Checking Types", 'cyan')
example_float = 3.14159
example_list = [1, 2, 3]
cprint(f"Type of {example_float}: {type(example_float)}", 'green')  # Output: <class 'float'>
cprint(f"Type of {example_list}: {type(example_list)}", 'green')  # Output: <class 'list'>

cprint('-'.center(40, '-'), 'magenta')

#* Custom Classes
# The type() function can also be used with custom classes.
class MyClass:
    pass

instance = MyClass()
cprint("Using type() with Custom Classes", 'cyan')
cprint(f"Type of instance of MyClass: {type(instance)}", 'green')  # Output: <class '__main__.MyClass'>

cprint('-'.center(40, '-'), 'magenta')

#* Type Comparison
# You can compare types using the type() function.
cprint("Type Comparison", 'cyan')
if type(example_int) == int:
    cprint("example_int is an integer", 'green')  # Output: example_int is an integer

cprint('-'.center(40, '-'), 'magenta')

#* Dynamic Type Checking
# Dynamic type checking can be useful in functions.
def dynamic_type_check(variable):
    if type(variable) == int:
        cprint(f"{variable} is an integer", 'green')
    elif type(variable) == str:
        cprint(f"{variable} is a string", 'green')
    else:
        cprint(f"Type of {variable}: {type(variable)}", 'green')

cprint("Dynamic Type Checking", 'cyan')
dynamic_type_check(example_int)  # Output: 42 is an integer
dynamic_type_check(example_str)  # Output: Hello, World! is a string

cprint('-'.center(40, '-'), 'magenta')

#* Using isinstance()
# The isinstance() function is an alternative for type checking.
cprint("Using isinstance()", 'cyan')
if isinstance(example_int, int):
    cprint("example_int is an integer (using isinstance)", 'green')  # Output: example_int is an integer (using isinstance)

cprint('-'.center(40, '-'), 'magenta')

#* Type of Built-in Functions and Methods
# The type() function can also be used with functions and methods.
def example_function():
    pass

cprint("Type of Built-in Functions and Methods", 'cyan')
cprint(f"Type of example_function: {type(example_function)}", 'green')  # Output: <class 'function'>
cprint(f"Type of cprint: {type(cprint)}", 'green')  # Output: <class 'function'>

cprint('-'.center(40, '-'), 'magenta')

#* Type of Lambda Functions
# Lambda functions also have a specific type.
lambda_function = lambda x: x + 1
cprint("Type of Lambda Functions", 'cyan')
cprint(f"Type of lambda_function: {type(lambda_function)}", 'green')  # Output: <class 'function'>

cprint('-'.center(40, '-'), 'magenta')

#* Advanced Example
# Combining type() with other built-in functions.
cprint("Advanced Example", 'cyan')
example_dict = {'a': 1, 'b': 2}
example_set = {1, 2, 3}
cprint(f"Type of example_dict: {type(example_dict)}", 'green')  # Output: <class 'dict'>
cprint(f"Type of example_set: {type(example_set)}", 'green')  # Output: <class 'set'>

# This is a comprehensive overview of the type() function and its usage in Python.