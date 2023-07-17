print("WElcome to the bill calculator")
bill = float(input("How much is the bill?"))
tip = int(input("How much did you tip? 1-->50%"))
people = int(input("How many people will split the bill?"))
total_bill_eachperson = bill*(tip/100 + 1) / people
print(f"Your bill of {bill}$ split amongst {people} people with {tip}% tip is {round(total_bill_eachperson, 2)}$ per person ")