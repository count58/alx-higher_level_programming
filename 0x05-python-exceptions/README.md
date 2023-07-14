=============================
README.md

Python - Exceptions
In this project, I learned handling errors and exceptions in Python with try and except.
=============================


An exception in Python is an event that occurs during the execution of a program that interrupts the normal flow of the program's instructions. When an error occurs in the program, Python creates an exception object. If not handled properly, this exception will then propagate up the call stack until it's caught and handled, or until it reaches the main program, at which point the program will terminate.

Here are a few common types of exceptions in Python:

- `ZeroDivisionError`: Raised when you try to divide by zero.
- `TypeError`: Raised when an operation is performed on an object of an inappropriate type.
- `ValueError`: Raised when a function receives an argument of the correct type but inappropriate value.
- `FileNotFoundError`: Raised when a file or directory is requested but doesn't exist.
- `KeyError`: Raised when a dictionary key is not found.

Here's an example of a simple exception:

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    x = 0
    print("Divided by zero, setting x to 0")
```

In this example, the `try` block is executed. When Python encounters the division by zero, it raises a `ZeroDivisionError` exception. The code then jumps out of the `try` block and into the `except` block, which handles the exception and prevents the program from crashing.

There's also a `finally` clause that can be added to the `try`/`except` block. Code inside the `finally` block will be executed no matter what, whether an exception is raised or not. This is often used for cleanup code that must be executed under all circumstances, like closing an open file.

```python
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print(f"OS error: {err}")
except ValueError:
    print("Could not convert data to an integer.")
finally:
    f.close()
    print("File is closed.")
```

In this example, the `try` block attempts to open a file, read a line, and convert it to an integer. If any of these steps fail, the appropriate exception will be raised. Regardless of whether an exception is raised or not, the `finally` block is executed, ensuring that the file is properly closed.


