#day1 task2
#bill details
total_bill = float(input("Enter total bill amount: "))
number_of_people = int(input("Enter number of people: "))
tip_percentage = float(input("Enter tip percentage: "))
#using arithmetic operators
tip_amount = (total_bill * tip_percentage) /100
final_bill = total_bill + tip_amount
amount_per_person = final_bill / number_of_people

extra_amount = total_bill % number_of_people
#result
print("\n--------------BILL DETAILS ------------------")
print(f"Bill Amount                 : ₹{total_bill}")
print(f"Tip Percentage              : {tip_percentage}")
print(f"Tip Amount                  : ₹{round(tip_amount, 2)}")
print(f"Final Bill                  : ₹{round(final_bill, 2)}")
print(f"Amount Per Person           : ₹{round(amount_per_person, 2)}")
print(f"Extra Amount                : ₹{round(extra_amount, 2)}")
print("-----------------------------------------------")
