# Fake Binary

Task:

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string

---

### Solution:

```python
def fake_bin(x):
    binary = ""
    for i in x:
        if int(i) < 5:
            binary += "0"
        else:
            binary += "1"
    return binary
```
