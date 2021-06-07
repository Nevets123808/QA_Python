def grade(homework, assessment, exam):
    finalresult = (homework*4 + assessment*2 + exam)/3
    print(f"Your final score is {finalresult}%")
    if finalresult > 90:
        grade ="A"
    elif finalresult > 80:
        grade = "B"
    elif finalresult > 70:
        grade = "C"
    elif finalresult > 50:
        grade ="D"
    else:
        grade = "Fail"
    print(f"That's a {grade}.")

homework = int(input("Please enter your homework mark (/25): "))
assessment = int(input("Please enter your assesment mark (/50): "))
exam = int(input("Please enter your exam mark (/100): "))
grade(homework, assessment, exam)