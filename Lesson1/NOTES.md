# Python Variables

## Table of content

- [Welcome to python variables](#python-variables)
- [Table of content](#table-of-content)
- [Variables in  python](#variable)
  - [Naming a variable](#naming-a-variable)
    - [Rules for naming variables](#a-variable-name-can)
  - [Naming conventions](#naming-conventions)
    - [Pascal casing](#1-pascalcasing)
    - [Camel casing](#2-camelcasing)
    - [Snake case](#2-snake_case)
## Variable

A variable is a **container or store** for storing data in a program. or a Variable is a **label** for data that can be assigned a value.

e.g

```python
name = "Roy"
age = 40
gender = "Male"
genderC = 'M'
tribe = "Batibo"
country = "Cameroon"
```

## Naming a variable

**NB: When naming a variable, follow these rules:**

### _A variable name can_

### 1. Start with an underscore or letter not number

```python
name1 = "John" 
# not 
1name = "John"

#Or
_name = "John"
# not 
1name = "John"
```

### 2. Contain only letters, underscores and numbers (No -, $ etc.)

```python
_name = "AfuhFlynn"
# not allowed
$name = "John"
```

### 3. Not contain white spaces

To avoid this, we use naming conventions (Pascal casing, camel casing, all lower case or underscores to separate words)

```python
my_name = "AfuhFlynn"

# not allowed
my name = "John"
```

### Naming conventions

#### 1. PascalCasing

Here, the first letter of every word in the variable name is capitalized (Not separated by spaces)

e.g

```python
MyName = "John Flynn"
```

#### 2. camelCasing

Here, the first letter of the variable name is always lower case

e.g

```python
myName = "John Flynn"
```

#### 2. snake_case

Here, all letters in the in the variable name are lower case. **It is avisiable to use underscores ( _ )** in naming variables to make it more readable

e.g

```python
alllongpigs = 80 # Not quit readable
# The preferred method
all_long_pigs = 80 # More readable.
```

**NB:** This is the most used naming convention in python.

## Variable type

The type of a variable is **The type of value or data it can store**

**_There are primarily 4 types of variables in python, each with or without subtypes:_**

### Number type

A number is a numerical value (10, 30, 0.4, etc.).
There a two types of numbers in python: **integers** and **floats**.

``` python
# integer
age = 19
# float
GPA = 4.8
print(age, GPA) # 19, 4.8
```

### Character type

A character is made up of a single alphabet, symbol, number, etc. (e.g a, b, 8, /, +, etc.).
Here, **We enclose the value in between single quotes ('8', 'a')**

``` python
# character
gender = 'M'
print(gender) # M
```

### Boolean type

A boolean is a type that can hold either of two values **i.e (True or False)**

``` python
# boolean
isFull = False

print(isFull) # False
print(isFull == False) # True
print(isFull == True) # False
```

### Object type

An object type is a type whose definition comes from combination of other types.
It is primarily made up of **(Strings, Lists, Dictionaries).**

#### String type

A string is a collection or combination or sequence of characters.
It is usually enclosed in between **single or double quotes: '' or ""**

```python
# String
name = "Afuh Flynn"
gender = 'Male'
year = "2025"
print(name, gender, year) # Afuh Flynn, Male, 2025
```

#### List type

A list is an ordered collection or combination of values.
It is usually enclosed in between **square brackets: []**

```python
# List
a = ["John", "Flynn", 8, 10, True, False]
## Here we use indexes to access values which will be explained in subsequent chapters
print(a[0]) # John
print(a[4]) # True
```

#### Dictionary type

A dictionary is an unordered collection or combination of **values pairs**.
**Each value has its unique key that identifies it e.g {name: "Afuh", age: 19}**
It is usually enclosed in between **curly braces: i.e {} e.g {key1: value1, key2: value2}**

```python
# List
a = {name: "Afuh", age: 19}
## Here we use indexes of key if found or dot (.) notation to access values which will be explained in subsequent chapters
print(a[name]) # Afuh
# or
print(a.name) # Afuh
print(a[age]) # 19
# or
print(a.age) # 19
```
