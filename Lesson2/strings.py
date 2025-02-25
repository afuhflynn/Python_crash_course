# Strings in python


# Author: Afuh Flyine Tembeng
# This is a collection of my work on explaining the concept of strings. (Each work here has it's own NOTES.md file)
## Contact:
# email: flyinnsafuh@gmail.com
# Github: https://github.com/AfuhFlynns
# Tel: +237675171796


# String
name = "Afuh Flynn" 
# Or
name = 'Afuh Flynn'

# This flexibility in strings allows us to do:
name = "My name's Afuh Flynn"
name = 'My quote: "My name is Afuh Flynn"'

print(name)

## Changing case with methods
# 1. The title() method. It capitalizes every first letter of words in the string
name = "john dalton"
print(name.title()) # A title has every first letter of every word capitalized

# 2. The upper() method. It changes all the letters to upper case
print(name.upper())

# 3. The lower() method. It changes all the letters to lower case
name = "TEMBENG MYLSE"
print(name.lower())

## Inserting variables into strings
## 1. Using the formatted strings (f-string) package
firstname = "Tembeng"
lastname = "Mylse"

fullname = f"{firstname} {lastname}"
print(fullname) # Tembeng Mylse

# Or
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# Stripping whitespaces
## 1. Using the rstrip() method (Removes the whitespaces on the right)
name = "Afuh Flynn "
print(name.rstrip()) # Afuh Flynn

## 2. Using the lstrip() method (Removes the whitespaces on the left)
print(name.lstrip()) # Afuh Flynn#

# 3. Using the strip() method (Removes the whitespaces on the left and right)
print(name.strip()) # Afuh Flynn

# 3. Using the strip() method (Removes the whitespaces on the left and right)
print(name.strip()) # Afuh Flynn


# Removing prefixes from strings
# This is done using the removeprefix() method which removes any starting point in the string provided in the paranthesis
flintai = "https://flintai.com"
print(flintai.removeprefix("https://")) # flintai.com

# Or
syntaxspring = "https://syntaxspring.io"
print(syntaxspring.removeprefix("https://")) # syntaxspring.io

# Avioding syntax errors with strings
# We use single quotes in double quotes and double quotes in single quotes
# Using single quotes in single quotes or double quotes in double quotes will cause an error if not escaped

# 1. Single quotes in double quotes
message = "AfuhFlynn's house is located at Buea"
print(message)

# 2. Double quotes in single quotes
message = 'Albert Einstein once said, “A person who never made a mistake never tried anything new”'
print(message)

# 3. Using the escape sequence (\' or \")
# This tells the intepreter that the string has not yet ended ignore this and continue to the next quote
message = 'AfuhFlynn\'s house is located at Buea'
print(message)

# This causes a syntax error:
# message = 'AfuhFlynn's house is located at Buea' # Statements must be separated by newlines or semicolonsPylance "Buea" is not defined
# print(message)

# NB: This only causes a syntax error in single quotes though but it's a good practice to insert single in double and vice versa

# This will still work
message = "Albert Einstein once said, “A person who never made a mistake never tried anything new”"
print(message)

