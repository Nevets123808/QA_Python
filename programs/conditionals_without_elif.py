mark = int(input("Enter your mark: "))

if mark > 85:
    print("Distinction")
if mark > 65 and mark <= 85:
    print("Pass")
if mark < 65:
    print("Fail")