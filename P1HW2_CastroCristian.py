#Cristian Castro
#April 5, 2026
#P1HW2
# Math programming
#

print("This program calculates and displays travel expenses")

budget= input("Enter Budget: ")

destination= input("Enter Your Travel Destination: ")

fuel= input("How much do you think you will spend on gas?: ")

accommodation= input("Approximately, how much will you need for accommodation/hotel?: ")

food= input("Last, how much do you need for food?: ")

print("------------Travel Expenses------------")

print("Location: ", destination)
print("Initial Budget: ", budget)
print("Fuel: ", fuel)
print("Accommodation: ", accommodation)
print("Food: ", food)
print("Total Expenses: ", int(fuel) + int(accommodation) + int(food))

print("Remaining Balance: ", int(budget) - (int(fuel) + int(accommodation) + int(food)))



