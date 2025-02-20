# Python Strings

## Table of content

- [Welcome to python strings](#python-strings)
- [Table of content](#table-of-content)
- [Strings in  python](#string)
  - [Multilined strings](#multilined-strings)
  - [Changing case with methods](#changing-case-with-methods)
    - [The title method](#1-the-title-method-it-capitalizes-every-first-letter-of-words-in-the-string)
    - [The upper method](#2-the-upper-method-it-changes-all-the-letters-to-upper-case)
    - [The lower method](#3-the-lower-method-it-changes-all-the-letters-to-lower-case)
  - [Inserting varibales into strings](#inserting-variables-into-strings)
  - [Stripping whitespace in strings](#stripping-whitespaces)
    - [The rstrip method](#1-using-the-rstrip-method)
    - [The lstrip method](#2-using-the-lstrip-method)
    - [The strip method](#3-using-the-strip-method)
  - [Removing prefixes from strings](#removing-prefixes-from-strings)
  - [Avoiding Syntax Errors with strngs](#avioding-syntax-errors-with-strings)
    - [Single quotes in double quotes](#1-single-quotes-in-double-quotes)
    - [Double quotes in single quotes](#2-double-quotes-in-single-quotes)
    - [Using the escape sequence](#3-using-the-escape-sequence)
  - [Exercise Details](#exercise-details)

## String

A string is a collection of characters and each character can be indexed to get it's value

NB: Strings in python can be written by using single or double quotes. This allows us to use
single quotes within double quotes an vice versa

Below, are examples of strings:

```python
# Creating a string with double quotes
name = "Afuh Flynn"
```

### Or

```python
# Creating a string with single quotes
name = 'Afuh Flynn'
```

## This flexibility in strings allows us to do

```python
name = "My name's Afuh Flynn" # Insert single qoute into double qoutes
print(name) # My name's Afuh Flynn
quote = 'My quote: "Imagination is the DNA of all inventions!"' # Insert double qoutes into single qoutes
print(quote) # My qoute: "My name is Afuh Flynn"
```

## Multilined strings

A multilined string is a string that spans across multiple horizontal rows

examples:

```python
# To create a multilined string, insert it into triple single quotes
message = '''
Once upon a time, there a lived a programmer named Joshua
Joshua lived in doors for years without any friends nor families
Joshua had just little time for fun and parties
Joshua was so determined that he became the first self made billionaire in his town
This shows us that smart learning and had work pays
It doesn't hurts to be alone working on your future
But it hurts to be alone when you waste your life impressing others
'''

print(message)
```

**_NB: Multilined strings are very useful. So take them serious_**

## Changing case with methods

### 1. The title() method. It capitalizes every first letter of words in the string

```python
name = "john dalton"
# A title has every first letter of every word capitalized
print(name.title()) # John Dalton
```

### 2. The upper() method. It changes all the letters to upper case

```python
name = "john dalton"
print(name.upper()) # JOHN DALTON
```

### 3. The lower() method. It changes all the letters to lower case

```python
name = "TEMBENG MYLSE"
print(name.lower()) # tembeng mylse
```

## Inserting variables into strings

### 1. Using the formatted strings (f-strings) package

Here, we use the f-strings package inbuilt into python: (e.g f"Your string" or f'Your string')

```python
firstname = "Tembeng"
lastname = "Mylse"

fullname = f"{firstname} {lastname}"
print(fullname) # Tembeng Mylse
```

We can also use f-strings to compose a sentence and then assign it to a variable

```python
firstname = "Tembeng"
lastname = "Mylse"

fullname = f"{firstname} {lastname}"
message = f"Hello, {fullname}!"
print(message) # Hello, Tembeng Mylse!
```

## Stripping Whitespaces

### 1. Using the rstrip() method

This method removes the whitespaces on the right

```python
name = "Afuh Flynn "
print(name.rstrip()) # Afuh Flynn
```

### 2. Using the lstrip() method

This method removes the whitespaces on the left

```python
name = "Afuh Flynn "
print(name.lstrip()) # Afuh Flynn
```

### 3. Using the strip() method

This method removes the whitespaces on the left and right

```python
name = " Afuh Flynn "
print(name.strip()) # Afuh Flynn
```

## Removing prefixes from strings

This is done using the removeprefix() method which removes any sequence of characters in the string provided in the paranthesis

```python
flintai = "https://flintai.com"
print(flintai.removeprefix("https://")) # flintai.com

# Or
syntaxspring = "https://syntaxspring.io"
print(syntaxspring.removeprefix("https://")) # syntaxspring.io
```

## Avioding syntax errors with strings

- We use single quotes in double quotes and double quotes in single quotes
- Using single quotes in single quotes will cause an error if not escaped
- Using double quotes in double quotes can be sometimes confusing

### 1. Single quotes in double quotes

```python
message = "AfuhFlynn's house is located at Buea"
print(message)
```

### 2. Double quotes in single quotes

```python
message = 'Albert Einstein once said, “A person who never made a mistake never tried anything new”'
print(message)
```

### 3. Using the escape sequence

```text
That is: ('\'' or "\""). We use the back slash character
```

 This tells the intepreter that the string has not yet ended ignore this and continue to the next quote

```python
message = 'AfuhFlynn\'s house is located at Buea'
print(message) # AfuhFlynn's house is located at Buea
```

**This causes a syntax error:**

```python
message = 'AfuhFlynn's house is located at Buea' # Statements must be separated by newlines or semicolons. "Buea" is not defined
print(message)
```

**_NB: This only causes a syntax error in single quotes though but it's a good practice to insert single in double and vice versa_**

**This will still work, but can be confusing sometimes if there is not enough syntax highlighting:**

```python
message = "Albert Einstein once said, “A person who never made a mistake never tried anything new”"
print(message) # Albert Einstein once said, "A person who never made a mistake never tried anything new"
```

## Exercise Details

Don't forget to check the exercises at: [Strings Practical exercises](./Exercises.txt) or it's solution at: [Solution](./solution.py)
