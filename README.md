# Python_Modules
#### This repository contains my best home made Python modules.

---
## [`constants`](constants.py)
This module allows you to use constants in Python. 

> ### *Example Usage:*
> ```python
> from constants import Constants as const
>
> # you can make a new Constant with any type as a value as long as it's a valid variable name ↙️
> const.new("variable_name", 1234)
> print(const.get("variable_name"))
>
> # But if you try to change it in any way, you'll get an error.
> const.new("variable_name", "resetting variable_name...")
> ```
>
> ### *Output:*
> <img width="750" height="205" alt="Screenshot_2025-11-04_at_4 01 41_PM-removebg-preview" src="https://github.com/user-attachments/assets/8c988ddc-5801-49a7-9aa1-dddad73c7c3f" />


## [`ansi_colors`](ansi_colors.py)
This module allows you to insert ANSI-compliant color codes into string objects.   

> ### *Example Usage:*
> ```python
> from ansi_colors import AnsiCodes, color_text
>
> file = "testing.txt"
>
> open(file, 'w').write("This is some text in the file\n\nThis is another paragraph.\n")
> 
> print("This is the contents of", file)
> 
> words = open(file).read()
> 
> print(color_text(words, AnsiCodes.FG_RED, AnsiCodes.BOLD))
> print(color_text("This is the end of the file", AnsiCodes.FG_BLUE, AnsiCodes.ITALIC))
> ```

> ### *Output:*
> <img width="300" alt="Output" src="https://github.com/user-attachments/assets/94aba68b-682c-4354-a40f-f953700729ef" />


## [`MutableTypes`](MutableTypes.py)
This module contains `MutableInt`, `MutableFloat`, `MutableStr`, and `MutableBool` classes. They are exactly what they sound like: mutable variations of `int`, `float`, `str`, and `bool`.
