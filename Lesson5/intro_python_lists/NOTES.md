# Python Lists

## Table of content

- [Welcome to python lists](#python-lists)
- [Table of content](#table-of-content)
- [Lists in  python](#lists)
  - [Accessing elements in a list](#accessing-elements-in-a-list)
    - [Index Positions Start at 0, Not 1](#index-positions-start-at-0-not-1)
  - [Exercise Details](#exercise-details)

## Lists

A list is a collection of items in a particular order. You can make a list that includes the letters of the alphabet, the digits from 0 to 9, or the names of all the people in your family. You can put anything you want into a list, and the items in your list don’t have to be related in any particular way.

> **_NB:_ In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas.**

- `Python lists a are ordered and elements can only be accessed on a specific order`

e.g:

```python
# A simple python list
 bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) # ['trek', 'cannondale', 'redline', 'specialized']
```

> Displaying the square brackets to your users isn't probably what you may want. _Hence we need to know how to access individual elements in the list as follows_

### Accessing elements in a list

Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired. To access an element in a list, write the name of the list followed by the index of the item enclosed in square brackets.

e.g:

```python
# A simple python list
 bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0]) # This outputs trek
```

#### Index Positions Start at 0, Not 1

Python considers the first item in a list to be at position 0, not position 1.
This is true of most programming languages

***NB:**
`The reason has to do with how the list operations are implemented at a lower level. If you’re receiving unexpected results, determine whether you are making a simple off-by-one error`

The second item in a list has an index of 1. Using this counting system, you can get any element you want from a list by subtracting one from its position in the list. For instance, to access the fourth item in a list, you request the item at index 3.

e.g:

```python
# A simple python list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1]) # Cannondale
print(bicycles[3]) # specialized.
```

**HINT:**
Python has a special syntax for accessing the last element in a list. By asking for the item at index -1, Python always returns the last item in the list:

e.g:

```python
# A simple python list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1]) # This outputs - specialized
```

### Using Individual Values from a List

You can use individual values from a list just as you would any other variable. For example, you can use f-strings to create a message based on a value from a list. Let’s try pulling the first bicycle from the list and composing a message using that value.

e.g:

```python
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].upper()}."
print(message) # My fist bicycle was a TREK
```

## Exercise Details

Don't forget to check the exercises at: [Lists Practical exercises](./Exercises.txt) or it's solution at: [Solution](./solution.py)
