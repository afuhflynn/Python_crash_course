# Python Comments

## Table of content

- [Welcome to python comments](#python-comments)
- [Table of content](#table-of-content)
- [Comments in  python](#comments)
  - [Using comments for documentation](#using-comments-for-documentation)
- [The Zen of Python, by Tim Peters](#the-zen-of-python)
  - [Exercise Details](#exercise-details)

## Comments

> Comments are very important in most programming languages. They are very helpful at explaining the complex features of a program and helps in future updates and maintainance.
> In python, anything that follows a hash (#) symbol is a comment.

e.g

```python
# Here is a comment
# name = "Afuh Flynn"
name = "Faith Francis"
print("Hello, world " + name)
```

> Running the code above outputs, 'Hello, world Faith Francis' and not 'Hello, world Afuh Flynn'. Because 'name = "Afuh Flynn"' is ignored by the python interpreter.

### Using comments for documentation

```python
# Explaining the use or outcome of each line with comments.
t_name = ["John", "Job", "Jack"] # Teachers' names. (Documenting with comments)
s_name = ["Flynn", "Faith", "Lenz", "Prisca"] # Students' names. (Helps in differentiating between the names)
```

## The Zen of Python

> These are set of rules that govern the way in which programmers should write clean, maintainable, and reusable python code.

To display these rules, do the following:

```python
import this # Imports the Zen of Python quotes by Tim Peters.
print(this)
# Outputs:
''' 
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
```

> Or using a python REPL:

```python
>>> import this # Press enter key and the quotes will be displayed.
# Output:
''' 
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
```

## Exercise Details

Don't forget to check the exercises at: [Comments Practical exercises](./Exercises.txt) or it's solution at: [Solution](./solution.py)
