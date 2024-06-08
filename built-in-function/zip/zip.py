
#? Allows merging 2 iterable objects if the len count is the same
from termcolor import cprint

a = [0, 1, 2, 3, 4, 5, 6, 7]
b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

#* Verify the len of the iterable
cprint(len(a), 'red')
cprint(len(b), 'blue')
zip_objects = zip(a, b)
cprint(zip_objects, 'cyan') # <zip object at 0x000001BEE4FBCC80>
cprint(type(zip_objects), 'light_green') #<class 'zip'>
cprint('-'.center(40, '-'), 'magenta')
cprint('-'.center(40, '-'), 'magenta')
# To iterate in vales merge only iterate the this form
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')
# (5, 'f')
# (6, 'g')
# (7, 'h')
for c, d in zip_objects:
    cprint(f'{c, d}', 'red')
    
print("Hola, mundo!", end=" :)")


