# Comment Operator
# Single line comments are written with a hash symbol (#).

# This is a comment explaining the next line of code
x = 10  # This is also a comment attached to a line of code

'''
Multi-line comments can be created using triple quotes.
These comments can span multiple lines and are often used for 
long explanations or documentation.
'''

# ---------------------------------------------------------------

# Keywords and Identifiers
# Keywords are reserved words in Python with special meanings.
# Identifiers are names given to variables, functions, or classes.

# Example of keywords (cannot be used as variable names)
# def, return, if, else, class, try, except, etc.

# Valid identifiers: Names you can give to variables, functions, classes, etc.
my_variable = 5
my_function = lambda x: x * 2
print(my_variable, my_function(3))

# Invalid identifier (would cause a syntax error)
# 1st_variable = 10  # Cannot start an identifier with a number

# ---------------------------------------------------------------

# Line continuation and statement separator operators
# Line continuation allows breaking long lines of code into multiple lines.
# The backslash (\) is used for line continuation.

long_string = "This is a very long string that is split across " \
              "multiple lines using the backslash character."

# Alternatively, parentheses can be used to continue lines in expressions.
sum_value = (
    1 + 2 + 3 + 4 + 5
)

# Statement separator: The semicolon (;) is used to separate multiple statements on the same line.
x = 10; y = 20; z = x + y  # This is allowed, but it's not recommended for readability.

print(long_string, sum_value, z)

# ---------------------------------------------------------------

# Arithmetic operations: +, -, /, //, %, *
# These are basic arithmetic operators in Python.

a = 15
b = 4

addition = a + b        # Addition
subtraction = a - b     # Subtraction
division = a / b        # True division (float result)
floor_division = a // b # Floor division (integer result)
modulo = a % b          # Modulo (remainder)
multiplication = a * b  # Multiplication

print(addition, subtraction, division, floor_division, modulo, multiplication)

# ---------------------------------------------------------------

# divmod() function
# The divmod() function takes two numbers and returns a tuple containing
# the quotient (floor division) and the remainder.

result = divmod(a, b)  # divmod(a, b) returns (quotient, remainder)
print(f"Quotient: {result[0]}, Remainder: {result[1]}")

# ---------------------------------------------------------------

# Compound operations
# Compound operators combine an arithmetic operation with an assignment.

# Example: Adding and assigning using compound operator (+=)
x = 5
x += 3  # Equivalent to x = x + 3
print(f"x after +=: {x}")

# Example: Subtracting and assigning using compound operator (-=)
y = 10
y -= 2  # Equivalent to y = y - 2
print(f"y after -=: {y}")

# Example: Multiplying and assigning using compound operator (*=)
z = 4
z *= 2  # Equivalent to z = z * 2
print(f"z after *=: {z}")

# Example: Dividing and assigning using compound operator (/=)
w = 20
w /= 4  # Equivalent to w = w / 4
print(f"w after /=: {w}")
