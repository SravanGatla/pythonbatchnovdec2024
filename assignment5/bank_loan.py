# Simple Interest Calculation
def calculate_simple_interest(P, R, T):
    SI = (P * R * T) / 100
    return SI

# Compound Interest Calculation
def calculate_compound_interest(P, R, T):
    CI = P * (1 + (R / 100)) ** T - P
    return CI

# Example usage for Simple Interest
principal = 5000
rate_of_interest = 5  # in percentage
time = 3  # in years

simple_interest = calculate_simple_interest(principal, rate_of_interest, time)
print(f"Simple Interest: ${simple_interest}")

# Example usage for Compound Interest
compound_interest = calculate_compound_interest(principal, rate_of_interest, time)
print(f"Compound Interest: ${compound_interest}")
