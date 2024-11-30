# Convert Decimal to Hexadecimal
def decimal_to_hexadecimal(n):
    return hex(n)

# Convert Decimal to Octal
def decimal_to_octal(n):
    return oct(n)

# Convert Hexadecimal to Decimal
def hexadecimal_to_decimal(n):
    return int(n, 16)

# Convert Octal to Decimal
def octal_to_decimal(n):
    return int(n, 8)

# Example usage
decimal_num = 255
print(f"Decimal {decimal_num} to Hexadecimal: {decimal_to_hexadecimal(decimal_num)}")
print(f"Decimal {decimal_num} to Octal: {decimal_to_octal(decimal_num)}")

hex_num = "0xff"
print(f"Hexadecimal {hex_num} to Decimal: {hexadecimal_to_decimal(hex_num)}")

octal_num = "377"
print(f"Octal {octal_num} to Decimal: {octal_to_decimal(octal_num)}")
