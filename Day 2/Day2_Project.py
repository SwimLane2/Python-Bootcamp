print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? £"))
tip = int(input("How much percentage tip would you like to give? 10, 12 or 15? %"))
split_bill = int(input("How many people to split the bill? "))
split_amount = total_bill * (1 + tip / 100) / split_bill
total_bill = round(split_amount, 2)
print(f"Each person should pay: £{total_bill}")