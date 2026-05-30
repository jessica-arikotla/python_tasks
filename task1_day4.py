def calculate_emi(principal, rate, years):
    rate = rate / (12 * 100)
    months = years * 12
    emi = (principal * rate * (1 + rate) ** months) / ((1 + rate ) ** months - 1)
    return emi
loan_amount =float(input("Enter Loan Amount: "))
interest_rate = float(input("Enter Intrest Rate (%): "))
tenure = int(input("Enter Loan Tenure(Years): "))
emi = calculate_emi(loan_amount,interest_rate,tenure)
print("Monthly EMI =", round(emi , 2))
   
