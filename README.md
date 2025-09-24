# Python_Modules
#### This repository contains my best home made Python modules.

---

## [`ansi_colors`](ansi_colors.py)
This module allows you to insert ANSI-compliant color codes into string objects.   

### *Example Usage:*
```python
from ansi_colors import AnsiCodes, color_text
file = "testing.txt"
print("This is the contents of", file)
words = open(file).read()
print(color_text(words, AnsiCodes.FG_RED, AnsiCodes.BOLD))
print(color_text("This is the end of the file", AnsiCodes.FG_BLUE, AnsiCodes.ITALIC))
```

## [`MutableTypes`](MutableTypes.py)
This module contains `MutableInt`, `MutableFloat`, `MutableStr`, and `MutableBool` classes. They are exactly what they sound like: mutable variations of `int`, `float`, `str`, and `bool`.
