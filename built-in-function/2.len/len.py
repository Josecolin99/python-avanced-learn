#? Explaining the len() function and its usage
from termcolor import cprint

#* Basic Usage
# The len() function returns the number of items (length) in an object.
cprint("Basic Usage", 'cyan')
example_list = [1, 2, 3, 4, 5]
cprint("Example List:", 'green')
cprint(example_list, 'yellow')
cprint("Length of Example List:", 'green')
cprint(len(example_list), 'yellow')  # Output: 5

cprint('-'.center(40, '-'), 'magenta')

#* Strings
# The len() function can be used to get the length of a string.
cprint("Using len() with Strings", 'cyan')
example_string = "Hello, World!"
cprint("Example String:", 'green')
cprint(example_string, 'yellow')
cprint("Length of Example String:", 'green')
cprint(len(example_string), 'yellow')  # Output: 13

cprint('-'.center(40, '-'), 'magenta')

#* Tuples
# The len() function can be used to get the length of a tuple.
cprint("Using len() with Tuples", 'cyan')
example_tuple = (1, 2, 3, 4)
cprint("Example Tuple:", 'green')
cprint(example_tuple, 'yellow')
cprint("Length of Example Tuple:", 'green')
cprint(len(example_tuple), 'yellow')  # Output: 4

cprint('-'.center(40, '-'), 'magenta')

#* Dictionaries
# The len() function can be used to get the number of key-value pairs in a dictionary.
cprint("Using len() with Dictionaries", 'cyan')
example_dict = {'a': 1, 'b': 2, 'c': 3}
cprint("Example Dictionary:", 'green')
cprint(example_dict, 'yellow')
cprint("Number of key-value pairs in Example Dictionary:", 'green')
cprint(len(example_dict), 'yellow')  # Output: 3

cprint('-'.center(40, '-'), 'magenta')

#* Sets
# The len() function can be used to get the number of elements in a set.
cprint("Using len() with Sets", 'cyan')
example_set = {1, 2, 3, 4, 5}
cprint("Example Set:", 'green')
cprint(example_set, 'yellow')
cprint("Number of elements in Example Set:", 'green')
cprint(len(example_set), 'yellow')  # Output: 5

cprint('-'.center(40, '-'), 'magenta')

#* Nested Data Structures
# The len() function can be used to get the length of nested data structures.
cprint("Using len() with Nested Data Structures", 'cyan')
nested_list = [[1, 2], [3, 4, 5], [6, 7]]
cprint("Nested List:", 'green')
cprint(nested_list, 'yellow')
cprint("Length of Nested List (number of inner lists):", 'green')
cprint(len(nested_list), 'yellow')  # Output: 3

cprint('-'.center(40, '-'), 'magenta')

#* Custom Objects
# Custom objects can also implement __len__() method to use len().
class CustomObject:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

cprint("Using len() with Custom Objects", 'cyan')
custom_obj = CustomObject([1, 2, 3, 4])
cprint("Custom Object Items:", 'green')
cprint(custom_obj.items, 'yellow')
cprint("Length of Custom Object Items:", 'green')
cprint(custom_obj.__len__(), 'yellow')  # Output: 4

cprint('-'.center(40, '-'), 'magenta')

#* Error Handling
# Using len() on an unsupported type will raise a TypeError.
cprint("Error Handling with len()", 'cyan')
try:
    cprint("Length of integer 5:", 'green')
    cprint(len(5), 'yellow')  # This will raise a TypeError
except TypeError as e:
    cprint(f"Error: {e}", 'red')  # Output: Error: object of type 'int' has no len()

# This is a comprehensive overview of the len() function and its usage in Python.
