## A Needle in the Haystack

**Definition**

Can you find the needle in the haystack?
Write a function `findNeedle()` that takes an `array` full of junk but containing one `needle`
After your function finds the needle it should return a message (as a string) that says:
`"found the needle at position "` plus the `index` it found the needle, so:

**Example (Input --> Output)**
```python
find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]) 
```
--> "found the needle at position 5" 

---

### Solution:

```python
def find_needle(haystack):
    if "needle" in haystack:
        index = haystack.index("needle")
        return f"found the needle at position {index}"
```
