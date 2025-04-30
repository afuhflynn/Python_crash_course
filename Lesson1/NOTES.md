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
