Colossal
=========

Larger than life (colossal) macros for python!

## Usage

### Jinja Templates

For jinja templating add `# -*- coding: jinja2 -*-` to the top of your module.
 
Note: The block start string is set to `"# {%"` in order to conform as much as possible to standard python code.

#### Example

```
# -*- coding: jinja2 -*-

# {% set attrs = ['a', 'b', 'c'] %}

class MyClass:
    def __init__(
        self,
        # {% for attr in attrs %}
        {{attr}},
        # {% endfor %}
    ):
        # {% for attr in attrs %}
        self.{{attr}} = {{attr}}
        # {% endfor %}
```

This code is transformed, once imported, into:

```python
class MyClass:
    def __init__(
        self,
        a,
        b,
        c,
    ):
        self.a = a
        self.b = b
        self.c = c
```

You can also use jinja templating to render certain parts of code in development/debugging only, e.g:

```
# -*- coding: jinja2 -*-
{% if DEBUG %}
import pdb; pdb.set_trace()
{% endif %}
```

The above code will be rendered only when the env variable `DEBUG` is set, in which case it will be rendered as:

```python
import pdb; pdb.set_trace()
```

### Macros

For macros add `# -*- coding: macro -*-` to the top of your module.

Defined macros:

* `dict@(x, y, z)` which expands to `dict(x=x, y=y, z=z)`
