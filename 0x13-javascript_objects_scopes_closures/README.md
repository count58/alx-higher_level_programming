0x13-javascript_objects_scopes_closures

JavaScript, an object is a collection of data and methods. Objects are created using the `new` keyword. For example, the following code creates an object called `myObject`:

```
const myObject = new Object();
```

The `myObject` object has no properties or methods by default. You can add properties and methods to the object using the dot notation. For example, the following code adds a property called `name` to the `myObject` object:

```
myObject.name = "John Doe";
```

The `name` property now has the value "John Doe". You can access the value of the `name` property using the dot notation. For example, the following code prints the value of the `name` property to the console:

```
console.log(myObject.name);
```

The output of the code is "John Doe".

A scope is a region of code where variables are accessible. There are three types of scopes in JavaScript:

* **Global scope:** The global scope is the outermost scope in a JavaScript program. Variables declared in the global scope are accessible from anywhere in the program.
* **Function scope:** The function scope is the scope of a function. Variables declared in the function scope are only accessible from within the function.
* **Block scope:** The block scope is the scope of a block of code. Variables declared in the block scope are only accessible from within the block.

A closure is a function that has access to the variables in its surrounding scope, even after the surrounding scope has been closed. Closures are created when a function is nested inside another function. For example, the following code creates a closure:

```
function outerFunction() {
  let name = "John Doe";

  function innerFunction() {
    console.log(name);
  }

  return innerFunction;
}

const innerFunction = outerFunction();
innerFunction();
```

The `innerFunction` function has access to the `name` variable, even though the `outerFunction` function has finished executing. The output of the code is "John Doe".

Closures are a powerful tool that can be used to create reusable code. They can also be used to implement private methods and variables.

TASKS

## Function Prototypes :floppy_disk:

Prototypes for functions written in this project:

| File               | Prototype                                               |
| ------------------ | ------------------------------------------------------- |
| `7-occurrences.js` | `exports.nbOccurences = function (list, searchElement)` |
| `8-esrever.js`     | `exports.esrever = function (list)`                     |
| `9-logme.js`       | `exports.logMe = function (item)`                       |
| `10-converter.js`  | `exports.converter = function (base)`                   |


## Tasks :page_with_curl:

* **0. Rectangle #0**
  * [0-rectangle.js](./0-rectangle.js): JavaScript script that defines an empty
  class `Rectangle`.

* **1. Rectangle #1**
  * [1-rectangle.js](./1-rectangle.js): JavaScript script that defines a class
  `Rectangle`. Builds on [0-rectangle.js](./0-rectangle.js) with:
    * Constructor that initializes instance attributes `width` and `height` with
    given parameters `w` and `h`.

* **2. Rectangle #2**
  * [2-rectangle.js](./2-rectangle.js): JavaScript script that defines a class
  `Rectangle`. Builds on [1-rectangle.js](./1-rectangle.js) with:
    * If provided `w` and `h` are less than or equal to `0`, creates an empty object.

* **3. Rectangle #3**
  * [3-rectangle.js](./3-rectangle.js): JavaScript script that defines a class
  `Rectangle`. Builds on [3-rectangle.js](./3-rectangle.js) with:
    * Instance method `print()` that prints the rectangle using the `X` character.

* **4. Rectangle #4**
  * [4-rectangle.js](./4-rectangle.js): JavaScript script that defines a class
  `Rectangle`. Builds on [4-rectangle.js](./4-rectangle.js) with:
    * Instance method `rotate()` that swaps the `width` and `height` of the `Rectangle`.
    * Instance method `double()` that multiplies the `width` and `height` of the
    `Rectangle` by `2`.

* **5. Square #0**
  * [5-square.js](./5-square.js): JavaScript script that defines a class `Square`
  that inherits from `Rectangle`.
    * Constructor takes one argument `size`.

* **6. Square #1**
  * [6-square.js](./6-square.js): JavaScript script that defines a class `Square`
  that inherits from `Rectangle`. Builds on [5-square.js](./5-square.js) with:
    * Instance method `charPrint(c)` that prints the `Square` using the character
    `c`.
    * If `c` is `undefined`, uses the character `X`.

* **7. Occurrences**
  * [7-occurrences.js](./7-occurrences.js): JavaScript function that returns the
  number of occurrences in a list.

* **8. Esrever**
  * [8-esrever.js](./8-esrever.js): JavaScript function that reverses a list.

* **9. Log me**
  * [9-logme.js](./9-logme.js): JavaScript function that prints the number of
  arguments already printed as well as the new argument value.
  * Output: `<number arguments already printed>: <current argument value>`

* **10. Number conversion**
  * [10-converter.js](./10-converter.js): JavaScript function that converts a number
  from base 10 to another base passed as argument.

* **11. Factor index**
  * [100-map.js](./100-map.js): JavaScript script that imports an array and creates
  a new array with each value equal to the value of initial list times the index of
  the new list.
  * Prints both the initial and new list.

* **12. Sorted occurences**
  * [101-sorted.js](./101-sorted.js): JavaScript script that imports a dictionary
  of occurrences by user ID and computes a new dictionary of user ID's by occurrences.
  * Prints the new dictionary.

* **13. Concat files**
  * [102-concat.js](./102-concat.js): JavaScript script that concatenates two files
  passed as arguments into a file specifed as the third argument.
  * Usage: `./102-concat.js fileA fileB fileC`.
