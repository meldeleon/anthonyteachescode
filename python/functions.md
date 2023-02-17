**Functions**
- there are two ways to define a function, one with `def function(arg):` and code block. the other is anonymous lambdas.
- in python, lambdas can only be a single expression.
- `lambda arg,arg2: arg + arg2`
- expression vs. statement: statement can only exist as a complete line. for example assignment in one statement, and must exist on its own line.  expression can appear anywhere(ish), `1+1` is an expression, but `return 5` is a statement.
- for lambdas the return is implied. 
- normal parameters in functions, can be called either positionally or by name
```python
def butts(param1, param2):
  print(f'this is the first param {param1}, this is the second {param2}')
butts("hamsters", "tuples")
butts(param2="tuples", param1="hamsters")
```
- if you call things with named arguments they don't have to be in order.
- parameters can have a default value defined.
```
def butts(param1='hamsters', param2='tuples'):
  print(f'this is the first param {param1}, this is the second {param2}')
- a parameter with a default cannot appear before a parameter that does not have a default.
- star splat parameter, `def function(*param1)` will collect all extra  positional arguments, passes it as a tuple.
```python
def f(*positionals, **animals):
  print(positionals, animals)
>>> f(1,2,cat="matcha", dog="tofu")
>>> (1,2) {"cat":"matcha", "dog":"tofu"}
```
- double star splat collects all extra named arguments and passes them in dict.
- a named only parameter appears after a start splat parameter
```python 
def f(a, *, b):
  pass
def f(*a, b):
  pass
```
- forces people to self document by using names for ambiguous things. helps escape boolean traps, forces you to name what the boolean value is.
- `/` parameters, everything to the left of it can only be passed positionally, but only by name
```python
def butts(param1, param2,/, param3):
  print(param1, param2, param3)
>>> butts(1,2,param3=3)
```
**QUIZ**
- make a function that takes a bunch of arguments and returns a comma separated string of all the arguments.

```python
def f(*args):
  return ', '.join(args) 
```

- implement a function that takes 2 positional only arguments without using a slash
```python
def f(*args):
  [param1, param2] = args
  print(param1, param2)
```  

