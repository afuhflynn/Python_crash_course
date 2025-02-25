from math import pi, log10, factorial # This imports the pi, log base 10 and factorial functions prebuilt into python
# Numbers in python


# Author: Afuh Flyine Tembeng
# This is a collection of my work on explaining the concept of numbers. (Each work here has it's own NOTES.md file)
## Contact:
# email: flyinnsafuh@gmail.com
# Github: https://github.com/AfuhFlynns
# Tel: +237675171796


# Number
# There are two types

age = 20 # Integer

score = 18.9 # Float

print(age, score)

## Underscores in numbers
universe_age = 14_000_000_000
print(universe_age) # 14000000000

## Basic operations with numbers in python
num1 = 2
num2 = 4

print(num1 + num2) # 6
print(num1 - num2) # -2
print(num1 * num2) # 8
print(num1 / num2) # 0.5

### Modulus operation (We use the % symbol)
mod = num1 % num2 # Returns the remainder of the dividing num1 by num2
print(mod) # 2

### Exponential and logarithmic and factorial operations
num = 4
print(num ** 2) # num ** 2 is equivalent to num^2 (outputs: 16)

print(log10(num)) # 0.6020599913279624

print(factorial(num)) # 4 * 3 * 2 * 1 = 24

### Python float and integer operations
## NB: Python by default prioritizes floats (It outputs a float for float and integer operations)
num = 20
frac = 10.43
print(num + frac) # 30.43
print(num - frac) # 9.57
print(num * frac) # 208.6
print(num / frac) # 1.9175455417066156


## Multiple Assignment
a, b, c = 3, 0, 2 # a = 3, b = 0, c = 2 (All variables are of same types)
print(a, b, c) # 3, 0, 2

## Constants in python
### A Constant is a variables whose value does not change through out the life time of a program (We use all uppercase characters)

MAX_AGE = 20
print(MAX_AGE)

