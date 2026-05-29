age = int(input("Enter age: "))
salary = int(input("Enter salary: "))
employment = input("Enter employment type(salaried/self-employed): ")

if age <21 or age > 60:
    print("Loan Rejected: Age not elibible")
elif salary < 25000:
    print("Loan Rejected: Salary should be minimum 25000")
elif employment != "salaried" and employment != "self-employed":
    print("Loan Rejected: Invalid employment type")
elif age >= 21 and age <= 30 and salary < 30000:
    print("Needs guarantor")
elif age > 55 and employment == "self-employed":
    print("High risk, senior review needed")
else:
    print("Loan Approved")
