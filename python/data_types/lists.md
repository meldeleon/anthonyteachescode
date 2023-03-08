
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
- `iadd` - stands for in-place add, can in-place add any iterable. 
```python
list_1 += [4]
print(list_1)
>>> [1,2,3,4]
```
- `imul` - stands for in-place multiply, will multiply the list and reassign it to variable (becuase it is mutable, unlike tuples)
- `reversed` allows you to iterate over an iterable backwards
```python
for i in list_1:
  print(i)
>>> 3
2
1
```
- `__setitem__` assigns a value to an index, if the index is out of range, it will throw an error.
- `append` will add an object to the end of the list, same as push()
```python
>>> list_1 = [1,2,3]
>>> list_1.append(4)
>>> list_1
[1, 2, 3, 4]
```
- `clear` will empty the list
```python
>>> list_1.clear()
>>> list_1
[]
```
- `copy` will return a shallow copy of a list 
```python
>>> list_1 = [[1,2],[2,3]]
>>> list_2 = list_1.copy()
>>> list_1[0][0] = 0
>>> list_2
[[0, 2], [2, 3]]
```
- `extend` will extend a list with an iterable
```python
>>> list_1 = [1,2,3]
>>> list_1.extend([4,5,6])
>>> list_1
[1, 2, 3, 4, 5, 6]
```
- `insert` takes an index and value to insert
```python
>>> list_1 = [1,2,3]
>>> list_1.insert(0,0)
>>> list_1
[0, 1, 2, 3]
```
- `pop` lets you remove a value from any index
```python
>>> list_1.pop(0)
0
>>> list_1
[1, 2, 3]
```
- `remove` will remove the first instance of a value from a list
```python
>>> list_1 = [1,2,3,1]
>>> list_1.remove(1)
>>> list_1
[2, 3, 1]
```
- `reverse` will reverse the list in place. 
```python
>>> list_1.sort()
>>> list_1
[1, 2, 3]
>>> list_1.sort(reverse=True)
>>> list_1
[3, 2, 1]
>>> list_2 = [2,3,-4,-1]
>>> list_2.sort(key = lambda x: abs(x))
>>> list_2
[-1, 2, 3, -4]
```

