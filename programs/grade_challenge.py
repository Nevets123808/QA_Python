grades = {"Maths":"", "Chemistry":"","Physics":""}
average = 0

for key in grades.keys():
    grades[key] = int(input(f"Please enter your {key} mark: "))
    average += grades[key]

average = average/len(grades.keys())

print(f"Your average score is {average}%")

if average > 70:
    score = "A"
elif average > 60:
    score = "B"
elif average > 50:
    score = "C"
elif average > 40:
    score = "D"
else:
    score = "You failed"

print(f"You scored a grade: {score}")