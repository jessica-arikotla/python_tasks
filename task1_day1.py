#Task1_day1
student_name = input("Enter name: ")
student_age = int(input("Enter age: "))
student_city = input("Enter city: ")
student_fav_subject = input("Enter favourite subject: ")
#Birth year calculation
birth_year = 2024 - student_age
#Profile details
print("\n--------- PROFILE CARD -----------------")
print(f"Name              :  {student_name}")
print(f"Age               :  {student_age}")
print(f"City              :  {student_city}")
print(f"Favourite Subject :  {student_fav_subject}")
print(f"Birth Year        :  {birth_year}")
print("-------------------------------------------")
