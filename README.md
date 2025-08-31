# intersperse

A simple Python generator that yields elements from an iterable, inserting a separator value between each element.

## Installation

```bash
pip install intersperse
```

## Usage

```python
# coding=utf-8
from intersperse import intersperse

# Intersperse zeros between numbers
print(list(intersperse([1, 2, 3], 0)))
# Output: [1, 0, 2, 0, 3]

# Works with any iterable
print(list(intersperse('abc', '-')))
# Output: ['a', '-', 'b', '-', 'c']

# Edge cases
print(list(intersperse([], 0)))
# Output: []

print(list(intersperse([1], 0)))
# Output: [1]
```

## License

MIT