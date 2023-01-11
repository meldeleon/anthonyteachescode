## str
- string type in python is `str`, typically made by literals or the str function.
-`__str__` str method which is how str converts other things into strings.

### magic methods
- methods with `__x__` are called magic methods, because python uses them as a part of the runtime, like operators etc.
- magic methods are called with `method("str")` 
- doc strings are special comments attached to a function that the help() mechanism can read in dead snakes.
- you can squacket and slice strings using `"butts"[0:4]`, also supports negative indexing, you can reverse a string using `"butts"[::-1]`, or get every nth character using `"butts"[::2]`
- strings are iterable, each iteration is one character strings.
- repr will show represenation of anything in string

### regular methods
- regular methods are called with `"string".method()`
- `count()` will count a substring
- `center()` will center a string in a given width
- `find()` is like indexOf in JS, and will return -1, `index()` will throw an exception
- `join()` concatenates strings, works directly on strings and any sort of iterable. It inserts the string whose method is called between every iterable item in its argument.  
- 
