#Cristian Castro
#April 12, 2026
#P2HW1
#This assignment will asses the students ability to edit and enhance exiting programs

#This program calculates and displays travel expenses
print(f'\nThis program calculates and displays travel expenses')
#Get the budget from user
budget = float(input(f"\nEnter Budget: $"))

#Get the destination from user
destination = input(f"\nEnter your travel destination: ")

#Get expected gas expenses from user
gas = float(input(f"\nHow much do you think you will spend on gas?: $"))

#Get expected accommodation expenses from user
accommodation = float(input(f"\nApproximately, how much will you need for accommodation/hotel?: $"))

#Get expected food expenses from user
food = float(input(f"\nLast, how much do you need for food?: $"))

print("\n------------Travel Expenses------------")
print(f'{"Location:":<15s} {destination}')
print(f'{"Initial Budget:":<15s} ${budget:,.2f}')
print(f'{"Fuel:":<15s} ${gas:,.2f}')
print(f'{"Accommodation:":<15s} ${accommodation:,.2f}')
print(f'{"Food:":<15s} ${food:,.2f}')
print("\n--------------------------------------")

print(f'{"Remaining Balance:":<15s} ${budget - (gas + accommodation + food):,.2f}')