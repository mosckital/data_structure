# Time Complexity of the Common Python Data Structure

The time complexity data are from the [Python Wiki Time Complexity](https://wiki.python.org/moin/TimeComplexity) page. Please refer to this page if necessary.

Different Python implementation may have different time complexities for the common Python data structures.
The time complexities in this note are the results of the current CPython, which is a typical and widely used Python implementation.
We could safely assume that the other Python implementations are not slower by more than a factor of **O(log n)**.

## `list`

`list` is one of the most fundamental data structure in Python.

We can use `list` as an `array` because this is how a `list` is internally represented.
We can use `list` as an `stack` as well because `list` supports O(1) complexity `append` and `pop` operations to the end of a list.

Please be aware that Python has an [`array` module](https://docs.python.org/3/library/array.html) to efficiently represent an array of basic values of a same type. This is less popular than `list` because it has less flexibility to gain efficiency and supports less data types.

### `list` operations time complexity

Operation | Average Case | Amortised Worst Case
---|---|---
Copy | O(n) | O(n)
Append | O(1) | O(1)
Pop last | O(1) | O(1)
Pop intermediate | O(k) | O(k)
Insert | O(n) | O(n)
Get item | O(1) | O(1)
Set item | O(1) | O(1)
Delete item | O(n) | O(n)
Iteration | O(n) | O(n)
Get Slice | O(k) | O(k)
Delete Slice | O(n) | O(n)
Set Slice | O(k+n) | O(k+n)
Extend | O(k) | O(k)
Sort | O(n log n) | O(n log n)
Multiply | O(nk) | O(nk)
x in s | O(n) |
min(s), max(s) | O(n) |
Get Length | O(1) | O(1)

## `deque`

`collections.deque` is internally implemented by a `doubly linked list` (in fact a list of array for greater efficiency). We can use it as a stack or a queue, or even more complex data structure which requires a doubly linked list as a base.

### `deque` operations time complexity

Operation | Average Case | Amortised Worst Case
---|---|---
Copy | O(n) | O(n)
append | O(1) | O(1)
appendleft | O(1) | O(1)
pop | O(1) | O(1)
popleft | O(1) | O(1)
extend | O(1) | O(1)
extendleft | O(1) | O(1)
rotate | O(k) | O(k)
remove | O(n) | O(n)

## `dict`

The `dict` is internally implemented by a `hash table`. It uses **open addressing** and **random probing** to solve the **hash collisions**, and it uses the combination of *hash value* and *key value* for look up of entry.

This [Stackoverflow](https://stackoverflow.com/a/9022835) answer gives a concise and excellent introduction to the details of the implementation.

There is also a fast-path for the dicts that only deal with `str` keys. Basically, if a dict only contains string keys, Python will skip some error checks and optimise some comparisons, which will make the execution faster. But do not optimise prematurely and often converting to string costs more than what optimisation saves.

This [Stackoverflow](https://stackoverflow.com/a/11162322) answer provides more details about this optimisation.

### `dict` operations time complexity

Operation | Average Case | Amortised Worst Case
---|---|---
Copy | O(n) | O(n)
Get Item | O(1) | O(n)
Set Item | O(1) | O(n)
Delete Item | O(1) | O(n)
Iteration | O(n) | O(n)

## `set`

The `set` has a very similar internal implementation as the `dict`, which is a `hash table`. So all the information in the previous section also apply here.

### `set` operations time complexity

Operation | Average Case | Worst Case
---|---|---
`x` in `s` | O(1) | O(n)
Union `s|t` | O(len(s)+len(t)) |
Intersection `s&t` | O(min(len(s),len(t)))`*` | O(len(s)*len(t))
Multiple intersection `s1&s2&..&sn` | | (n-1)*O(l) where l is max(len(s1),...,len(sn))
Difference `s-t` | O(len(s)) |
`s.difference_update(t)` | O(len(t)) |
Symmetric Difference `s^t` | O(len(s)) | O(len(s)*len(t))
`s.symmetric_difference_update(t)` | O(len(t)) | O(len(t)*len(s))

`*`: replace `min` with `max` if `t` is not a `set`
