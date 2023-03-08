## dicts 
- a dict is hash map, a table that maps keys to values. In JS it is an object.
- in js, you can only have objects with string keys. but in python a key can be anything that is hashable. tuples are hashable if everything inside of it are hashables. lists are not because the are mutable. empty tuples take the default hash value. ints, floats, bools, nones and complex numbers are also hashable.
```python
teams = {'butts': ['mel', 'xzeroknight', 'benderminguez'], 'boobs': ['anthony']}
```
- dict() - initialized an empty dict, dict(mapping) allows you to create a dict based on other mapping data types.
- dict(iterable) - initialize a dict on an iterable, the iterable must be in the format [[k,v],[k1, v1],[k2,v2]
- dict(one=1, two=2) - will make am dictionary based on kwargs.
- contains `key in dict`, will return boolean if key is in dict
- ```python
new_dict = dict(one=1, two=2)
del dict['one'] 
```
- you cannot compare dicts, except for equality and not equal, ==, != will evalue T/F
- __getitem__, allows you to get a value from key
```python
>>> new_dict = dict(one=1, two=2)
>>> new_dict["two"]
2
```
- `|` can be used to combine two dictionaries, if there are conflicting keys, it will be the last value in saved.
```python
>>> new_dict = dict(one=1, two=2)
>>> new_dict_2 = dict(three=3, four=4)
>>> new_dict | new_dict_2
{'one': 1, 'two': 2, 'three': 3, 'four': 4}
``` 
- `|=` or in place will add a dict to another dict in place, this was never implmented for lists. 
```python
>>> new_dict = dict(one=1, two=2)
>>> new_dict_2 = dict(three=3)
>>> new_dict |= new_dict_2
>>> new_dict
{'one': 1, 'two': 2, 'three': 3}
```
- iterating over a dict returns its keys, not key values
- `len(dict)`returns the number of kvps.
```python
>>> len(new_dict)
3
```
- reversed lets you iterate over keys in a dict
```python
>>> for key in reversed(new_dict):
...     print(key)
... 
three
two
one
```
- ror is right-hand or, or if the left-side is a mapping that is not a dictionary. will return a dictionary.
- __setitem__, you can assign a value to a key in dict
```python
>>> new_dict["five"] = 5
>>> new_dict
{'one': 1, 'two': 2, 'three': 3, 'five': 5}
```
- `clear` empties the dict
```python
>>> new_dict.clear()
>>> new_dict
{}
```
- `copy` creates a shallow copy
```python
>>> new_dict = new_dict_2.copy()
>>> new_dict
{'three': 3}
```
- `get` returns a value by key, takes an optional second positional parameter default reurn value.
```python
>>> new_dict.get("one")
1
>>> new_dict.get("four", "one")
'one'
```
- `D.items()` provides a set like obj on dictionary items
```python
>>> for k,v in new_dict.items():
...     print(k,v)
... 
one 1
two 2
```
- `D.keys()` provides a set like obj on dict keys, just use base iteration.
```python
>>> for k in new_dict.keys():
...     print(k)
... 
one
two
```
- `pop(key)` will remove a specific key values, takes an optional second parameter return default.
```python
>>> new_dict["four"] = 4
>>> new_dict.pop("four")
4
>>> new_dict.pop("pussy","one")
'one'
>>> new_dict
{'one': 1, 'two': 2}
```
- small dicts optimization, dicts became ordered and it made them smaller. released in 3.6, new methods came in 3.8
- `popitem()` removes the LIFO item, and returns a tuple (k,v).
```python
>>> new_dict
{'one': 1, 'two': 2}
>>> new_dict.popitem()
('two', 2)
>>> new_dict
{'one': 1}
```
- `setdefault()` takes a key and a default, if key does not exist it sets that key to the default value and returns the default. if the key does exist it returns the value of theat key value.

```python
>>> new_dict.setdefault("three", 3)
3
>>> new_dict
{'one': 1, 'two': 1, 'three': 3}
>>> new_dict.setdefault("three", 4)
3
```  
- `update()` takes an iterable and appends it to the dictionary.
- `D.values` shows a view of keys values in iteration
```python
>>> for v in new_dict.values(): 
...   print(v)
... 
1
1
3
```
- `dict.fromkeys()` lets you create a dict from an iterable, takes an interable and optional default val
```python
>>> loost = ["one", "two", "three"]
>>> new_dict_3 = dict.fromkeys(loost, "default")
>>> new_dict_3
{'one': 'default', 'two': 'default', 'three': 'default'}
>>> new_dict_3 = dict.fromkeys(loost)
>>> new_dict_3
{'one': None, 'two': None, 'three': None}
```
- `**` splat is a spread operator on dicts
 
