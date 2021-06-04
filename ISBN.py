number = input("please enter the first 12 digits: ")
sum = 0
for index in range(12):
    if index%2 == 0:
        sum += int(number[index])
    else:
        sum += int(number[index])*3

final_digit = 10- sum%10

print(f"The ISBN is {number}{final_digit}")
