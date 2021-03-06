# Ones and Zeros

Given an array of ones and zeroes, convert the equivalent binary value to an integer.

```
Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
```

Examples:

```
Testing: [0, 0, 0, 1] ==> 1
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 0, 1] ==> 5
Testing: [1, 0, 0, 1] ==> 9
Testing: [0, 0, 1, 0] ==> 2
Testing: [0, 1, 1, 0] ==> 6
Testing: [1, 1, 1, 1] ==> 15
Testing: [1, 0, 1, 1] ==> 11
```

However, the arrays can have varying lengths, not just limited to 4.

---

### Solution 1:

```python
def binary_array_to_number(arr):
    pow = len(arr)-1
    sum = 0
    for i in arr:
        if i == 1:
            sum += 2 ** pow
            pow -= 1
        else:
            pow -= 1
    return sum
```

### Solution 2:

```python
def binary_array_to_number(arr):
    return sum( 2**i for i, n in enumerate( arr[ ::-1 ] ) if n > 0 )
```
