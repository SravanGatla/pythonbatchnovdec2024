def calculate_simple_interest(P, R, T):
    SI = (P * R * T) / 100
    return SI

# Example usage
principal = 1500
rate_of_interest = 4  # in percentage
time = 2  # in years

simple_interest = calculate_simple_interest(principal, rate_of_interest, time)
print(f"Simple Interest: ${simple_interest}")
