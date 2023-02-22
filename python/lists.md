## Lists ##
- it's an array.
- you can create a list with squackets `new_list = [1,2]`
- you can create a list from an iterable (just like a tuple)
- `list(iterable=(), /)` takes one positional argument or nothing.
- `__delitem__` will delete a specifc item in a list (technically it removes a refrence count at index x and move everything over) 
```python
list_1 = [1,2,3]
del list[1]
print(list_1)
>>> [1,3]
```
- iadd - stands for in-place add, can in-place add any iterable. 
```python
list_1 += [4]
print(list_1)
>>> [1,2,3,4]
```

