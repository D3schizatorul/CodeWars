# Century From Year

The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

Given a year, return the century it is in.

Examples

```
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
```

---

### Solution 1:

```python
from math import ceil
def century(year):
    return ceil(year / 100)
```

### Solution 2:

```python
def century(year):
    return (year + 99) // 100
```
