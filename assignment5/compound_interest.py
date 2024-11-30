def calculate_compound_interest(P, R, T):
    CI = P * (1 + (R / 100)) ** T - P
    return CI

# Example usage
principal = 1500
rate_of_interest = 5  # in percentage
time = 3  # in years

compound_interest = calculate_compound_interest(principal, rate_of_interest, time)
print(f"Compound Interest: ${compound_interest}")
