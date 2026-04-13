#Cristian Castro
#April 12, 2026
#P2HW2
#Asses students understanding of lists


#ask the user to enter grades for each module
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

#Make grades as a list
module_grades = [module1, module2, module3, module4, module5, module6]

print("\n------------Results------------")

#calculate results
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

#display results
print(f"{'Lowest Grade:         ':15s}{lowest_grade:.1f}")
print(f"{'Highest Grade:        ':15s}{highest_grade:.1f}")
print(f"{'Sum of Grades:        ':15s}{total:.1f}")
print(f"{'Average:              ':15s}{average:.2f}")

print("-------------------------------")