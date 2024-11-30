def calculate_savings(initial_savings, monthly_deposit, months):
    total_savings = initial_savings + (monthly_deposit * months)
    return total_savings

# Example usage
initial_savings = 1000  # Initial savings in dollars
monthly_deposit = 200   # Monthly deposit in dollars
months = 12             # Period in months (1 year)

total = calculate_savings(initial_savings, monthly_deposit, months)
print(f"Total savings after {months} months: ${total}")
