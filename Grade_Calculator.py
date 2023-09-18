from operator import le


grade_percentage = int(input("Insert grade percentage: "))
letter = 0
if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80:
    letter = "B"
elif grade_percentage >= 70:
    letter = "C"
elif grade_percentage >= 60:
    letter = "D"
else: 
    letter = "F"

print (f"Your grade is {letter}")

if grade_percentage >= 70:
    print("Congratulation!!")
else:
    print("Study more next time :I")
   