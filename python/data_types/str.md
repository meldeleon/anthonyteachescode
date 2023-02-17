## str
- string type in python is `str`, typically made by literals or the str function.
-`__str__` str method which is how str converts other things into strings.

### magic methods
- methods with `__x__` are called magic methods, because python uses them as a part of the runtime, like operators etc.
- some magic methods are called with `method("str")`, but some are operators whihc are called like operators.
- doc strings are special comments attached to a function that the help() mechanism can read in dead snakes.
- you can squacket and slice strings using `"butts"[0:4]`, also supports negative indexing, you can reverse a string using `"butts"[::-1]`, or get every nth character using `"butts"[::2]`
- strings are iterable, each iteration is one character strings.
- repr will show represenation of anything in string

### regular methods
- regular methods are called with `"string".method()`
- `count()` will count a substring
- `center()` will center a string in a given width, `ljust()` left justifies and right pads a string with a given width, `rjust()` right justifies and left pads a string with a given width. `zfill` will fill a string with 0s for a given number of characters.
- `find()` is like indexOf in JS, and will return -1, `index()` will throw an exception
- `join()` concatenates strings, works directly on strings and any sort of iterable. It inserts the string whose method is called between every iterable item in its argument.
- `lstrip()`- remove lefthand whitespace, `rstrip()` - remove righthand whitespace, `strip()` - removes both; can take an argument to remove specific sequence of characters. Please note that it will remove any of those characters in the string, and is not looking for a specific sequence of characters.
- `removeprefix()` and `removesuffix()` will remove a specific sequence of characters at the beginning or end of a string
- `partion()`, will search for a partition, and if it finds it will return a tuple with the characters before, the partition, and after. if it's not found just returns the string.
- `replace()`, replaces all (finds all instances of a character or sequence of characters).
- `split()` returns all substrings seperated by a separator, returns list of substring
without a separator is splits on whitespace.
- `splitlines()`splits on line breaks only. agnostics for types of new lines.
- `lower()` `upper()` `capitalize()` `title()` - changes case of string.
- ways to define strings: single quote, double quote, triple quote ('''x'''), raw strings (r'xn\n'), f strings (f'x{butts+1}'); you can also combine raw and f strings (rf'xn\{butts}'). Unicode streams can be instantiated with a u, but all string in python 3 are unicode streams, so this does nothing.
- implicit string joining, `'x''y'` will become `'xy'`
