income = float(input("Enter Annual Income: "))
def calculate_tax(income):
    tax = 0
    if income >250000:
        taxable = min(income, 500000) - 250000
        tax += taxable * 0.05

    if income > 500000:
        taxable = min(incom, 1000000) - 500000
        tax += taxable * 0.20
        
    if income > 1000000:
        taxable = income - 1000000
        tax += taxable * 0.30
    return tax
tax = calculate_tax(income)
print("Total Tax =", tax)
        
