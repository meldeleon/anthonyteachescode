**Imports**
- there are two types of imports, `import alias`, an alias in this case is a dotted name, with an option to import `something as something_else`. The following syntaxes are allowed:
```python
import a,b
import a as c, b as d
import a.b.c
import a.b.c as d
```
- imports of python are a hierarchy, they make modules available and then assign a name. `import a.b.c` will make a.b.c available but assigns a to the module a, but `import a.b.c as d` will make a.b.c available but assign the c module to d.- from imports `from dotted.modules import list_of_name_aliases` plucking names out of dotted module.
- ways to instantiate join 
```python
from os.path import join
>>> join
from os import path
>>> os.path.join
- `from module import *` will import all name spaces from a module, but this gets tricky, not recommended.
