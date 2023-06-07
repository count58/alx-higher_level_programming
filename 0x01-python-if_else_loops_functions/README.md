0x01. Python - if/else, loops, functions

Sure, let's break down those elements as they apply to Python, which is a high-level, interpreted, general-purpose programming language:

1. **if/else**: These are conditional statements in Python. They allow the program to execute different blocks of code based on certain conditions being met.

   In this example, the program will print "x is positive" because the condition (`x > 0`) is true. If x was less than or equal to zero, it would print "x is not positive."


2. **Loops**: Loops in Python are used to execute a block of code repeatedly. Python has two types of loops: `for` and `while`.

   - **For loop**: This type of loop is used when you want to perform a block of code a certain number of times.
   
      This program will print the numbers 0 through 4, because `range(5)` generates a sequence of numbers from 0 to 4.

   - **While loop**: This type of loop keeps executing as long as a condition is met.

     This program will also print the numbers 0 through 4, because it keeps looping as long as `i` is less than 5.


3. **Functions**: In Python, a function is a named sequence of statements that perform a computation. You can define your own functions using the 'def' keyword.
   
     In this example, a function named `greet` is defined. It takes one parameter, `name`. When called, it returns a greeting string. 

     The `print(greet("Alice"))` line calls the function with "Alice" as the argument, and it will print "Hello, Alice".

These are fundamental concepts in Python and most other programming languages, so understanding them is crucial to becoming proficient in Python.


TASKS

0. Positive anything is better than negative nothing**
  * [0-positive_or_negative.py](./0-positive_or_negative.py): Python program that assigns
  a random signed number to the variable `number` each time it is executed and
  prints whether `number` is positive or negative.
  * Prints the number followed by:
    * If the number is greater than 0: `is positive`
    * If the number is 0: `is zero`
    * If the number is less than 0: `is negative`
    * Followed by a new line.

2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game**
  * [2-print_alphabet.py](./2-print_alphabet.py): Python program that prints the alphabet
  in lowercase, not followed by a new line.
  * Using only one `print` and one loop.
  * Without storing characters in variables or importing modules

3. When I was having that alphabet soup, I never thought that it would pay off**
  * [3-print_alphabt.py](./3-print_alphabt.py): Python program that prints the
  alphabet in lowercase, followed by a new line.
  * Using only one `print` and one loop.
  * Without storing characters in variables or importing modules.
  * Prints every letter except for `q` and `e`.

4. Hexadecimal printing**
  * [4-print_hexa.py](./4-print_hexa.py): Python program that prints all numbers from
  `0` to `98` in decimal and hexadecimal.
  * Using only one `print` and one loop.
  * Without storing numbers or strings in variables or importing modules.
  * Printing format: `[decimal] = [hexadecimal]`

5. 00...99**
  * [5-print_comb2.py](./5-print_comb2.py): Python program that prints numbers from `0`
  to `99` two digits each.
  * Numbers are separated by `, `, except for the last number, which is followed by a new line.
  * Using no more than two `print` functions and one loop.
  * Without storing numbers or strings in variables or importing modules.

5. 00...99
Write a program that prints numbers from 0 to 99.

Numbers must be separated by ,, followed by a space
Numbers should be printed in ascending order, with two digits
The last number should be followed by a new line
You can only use no more than 2 print functions with string format
You can only use one loop in your code
You are not allowed to store numbers or strings in a variable
You are not allowed to import any module

6. Inventing is a combination of brains and materials. The more brains you use, the less material you need**
  * [6-print_comb3.py](./6-print_comb3.py): Python program that prints all possible
  different combinations of two digits in ascending order.
  * Numbers are separated by `, `, except for the last number, which is followed by a new line.
  * The two digits must be different - `01` and `10` are considered identical.
  * Using no more than three `print` functions and two loops.
  * Without storing numbers or strings in variables or importing modules.

7. islower
Write a function that checks for lowercase character.

Prototype: def islower(c):
Returns True if c is lowercase
Returns False otherwise
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()
Tips: ord()
You don’t need to understand __import__

8. To uppercase
Write a function that prints a string in uppercase followed by a new line.

Prototype: def uppercase(str):
You can only use no more than 2 print functions with string format
You can only use one loop in your code
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()
Tips: ord()
You don’t need to understand __import__

9. There are only 3 colors, 10 digits, and 7 notes; its what we do with them that's important**
  * [9-print_last_digit.py](./9-print_last_digit.py): Python function that prints the last
  digit of a number.
  * Returns the value of the last digit.
  * Without importing modules.

10. a + b**
Write a function that adds two integers and returns the result.
  * [10-add.py](./10-add.py): Python function that returns the addition of two integers.
  * Without importing modules.
Prototype: def add(a, b):
Returns the value of a + b
You are not allowed to import any module
You don’t need to understand __import__

11. a ^ b**
  * [11-pow.py](./11-pow.py): Python function that returns `a` to the power of `b`.
  * Without importing modules.

12. Fizz Buzz
Write a function that prints the numbers from 1 to 100 separated by a space.

For multiples of three print Fizz instead of the number and for multiples of five print Buzz.
For numbers which are multiples of both three and five print FizzBuzz.
Prototype: def fizzbuzz():
Each element should be followed by a space
You are not allowed to import any module
You don’t need to understand __import__

13. Insert in sorted linked list**
  * [13-insert_number.c](./13-insert_number.c): C function that inserts a number
  into a sorted linked list.
  * If the function fails, returns `NULL`.
  * Otherwise, returns the address of the new node.
  * Helper files:
    * [linked_lists.c](./linked_lists.c): C functions handling linked lists for testing
    [13-insert_number.c](./13-insert_number.c) (provided by Holberton School).
    * [lists.h](./lists.h): Header file containing definitions and prototypes for
    all types and functions used in [linked_lists.c](./linked_lists.c) and
    [13-insert_number.c](./13-insert_number.c).

14. Smile in the mirror**
  * [100-print_tebahpla.py](./100-print_tebahpla.py): Python program that prints the alphabet
  in reverse order, alternating lowercase and uppercase, not followed by a new line.
  * Using only one `print` and one loop.
  * Without storing characters in variables or importing modules.

15. Remove at position**
  * [101-remove_char_at.py](./101-remove_char_at_py): Python function that
  creates a copy of a string without the character at position `n`.
  * Without importing modules.

16. ByteCode -> Python #2**
  * [102-magic_calculation.py](./102-magic_calculation.py): Python function matching exactly a
  bytecode.


=======================
