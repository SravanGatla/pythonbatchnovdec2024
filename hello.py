# class_01/hello.py

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b if b != 0 else "Division by zero error"


print("Calculator")
x = 10
y = 20
print("Addition:", add(x, y))
print("Subtraction:", subtract(x, y))
print("Multiplication:", multiply(x, y))
print("Division:", divide(x, y))


# Shebang line
# The shebang line is used to tell the operating system which interpreter to use to run the script.


# ---------------------------------------------------------------

# Indentation issue and Best practices
# In Python, indentation is crucial as it defines the structure of the code.
# Always use 4 spaces for indentation. Never mix tabs and spaces.

def greet(name):
    # This is a properly indented function
    print(f"Hello, {name}!")  # This print statement is inside the function
    # Indentation error would occur if we misaligned the line below.
    if name:
        print(f"Welcome, {name}!")
    return

greet("John")

# ---------------------------------------------------------------

# Built-in functions

# Example: Using the `len()` function to get the length of a string
message = "Hello, Python!"
print(f"Length of message: {len(message)}")  # len() is a built-in function

# Example: Using the `max()` function to find the largest number
numbers = [1, 5, 3, 9, 2]
print(f"Largest number: {max(numbers)}")  # max() is a built-in function

# ---------------------------------------------------------------

# Print function


print("This is a string.")  # Prints a string
print(12345)                # Prints an integer
print([1, 2, 3, 4])         # Prints a list

# You can also use formatted string literals (f-strings) to print values
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")  # f-string formatting

# ---------------------------------------------------------------

# Ascii and Unicode characters
# Python can handle both ASCII and Unicode characters, allowing you to work with various languages and symbols.

# Example: ASCII characters (range 0-127)
ascii_char = chr(65)  # ASCII value 65 corresponds to the letter 'A'
print(f"ASCII character for 65: {ascii_char}")

# Example: Unicode characters (support for international characters)
unicode_char = "你好"  # Chinese characters for "Hello"
print(f"Unicode characters: {unicode_char}")

# Using Unicode characters by their code point (e.g., for a heart symbol)
heart_symbol = "\u2764"  # Unicode for the heart symbol
print(f"Heart symbol: {heart_symbol}")

# ---------------------------------------------------------------

