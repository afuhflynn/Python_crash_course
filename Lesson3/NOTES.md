# Python Numbers

## Table of content

- [Welcome to python numbers](#python-numbers)
- [Table of content](#table-of-content)
- [Numbers in  python](#numbers)
  - [Types of numbers in python](#types-of-numbers)
    - [Integer numbers](#integer-numbers)
    - [Float numbers](#float-numbers)
  - [Underscores in numbers](#underscores-in-numbers)
  - [Basic operations with numbers](#basic-operations-with-numbers-in-python)
    - [Modulus operations](#modulus-operation)
    - [Exponential, logarithmic and factorial operations](#exponential-and-logarithmic-and-factorial-operations)
    - [Float and Integer operations](#python-float-and-integer-operations)
  - [Multiple assignment](#multiple-assignment)
  - [Constants in python](#constants-in-python)
  - [Exercise Details](#exercise-details)

## Numbers

We can say a number is a quantitative representation of data.

_There are two types of numbers in python:_

### Types of numbers

- Integer numbers
- Floating point numbers (decimal point numbers)

#### Integer numbers

These are whole number values with no decimal points.
e.g

```python
age = 19
children = 4 or 5
wives = 1
print(age, children, wives) # 19, 4, 1
```

#### Float numbers

These are whole number values with decimal points.
e.g

```python
score = 19.8
GPA = 4.5
temperature = 37.8
print(score, GPA, temperature) # 19.8, 4.5, 37.8
```

### Underscores in numbers

To allow for easire representation and readability of numbers, python allows developers/programmers to insert
underscores in lengthy numbers to improve readability.

e.g

```python
universe_age = 14_000_000_000
print(universe_age) # 14000000000
```

**NB: _Before storing the number, python removes the underscores and stores the actual value in memory_. That's why the output has no underscores in it.**

### Basic operations with numbers in python

In python, we can perform the mathematical operations (+, -, /, x, Mod, Exponents, Logarithms and more) with numbers.

e.g

```python
num1 = 2
num2 = 4

print(num1 + num2) # 6
print(num1 - num2) # -2
print(num1 * num2) # 8
print(num1 / num2) # 0.5
```

#### Modulus operation

In this case, we use the % symbol.

e.g

```python
mod = num1 % num2 # Returns the remainder of the dividing num1 by num2
print(mod) # 2
```

#### Exponential and logarithmic and factorial operations

In this case, we can either use in-built python modules Or we write the code manually

- **import the pi, log10 or log and factorial from math module functions in built into python**

- **For convenience purposes, we will make use of the in-built functions and write the code manually in advance topics (loops, conditionals)**

```python
from math import pi, log10, factorial # Inbuilt functions in the python math module
num = 4
print(num ** 2) # num ** 2 is equivalent to num^2 (outputs: 16)

print(log10(num)) # 0.6020599913279624

print(factorial(num)) # 4 * 3 * 2 * 1 = 24
```

#### Python float and integer operations

##### _NB: Python by default prioritizes floats (It outputs a float, for float and integer operations)_

```python
num = 20
frac = 10.43
print(num + frac) # 30.43
print(num - frac) # 9.57
print(num * frac) # 208.6
print(num / frac) # 1.9175455417066156
```

### Multiple Assignment

It is possible to assign multiple variables on the same line. But it is always preferable to do this with variables of the same type to avoid erros. **(It can still work with variables of different types though!!).**

```python
# Variables of the same types
a, b, c = 3, 0, 2
print(a, b, c) # 3, 0, 2
```

## Constants in python

A Constant is a variables whose value does not change through out the life time of a program **(We use all uppercase characters).**

e.g

```python
MAX_AGE = 20
print(MAX_AGE) # 20
```

## Exercise Details

Don't forget to check the exercises at: [Numbers Practical exercises](./Exercises.txt) or it's solution at: [Solution](./solution.py)
