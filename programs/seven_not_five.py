result = []
for number in range(2000,3201):
    if number%7 == 0 and number%5 != 0:
        result.append(str(number))
final =", ".join(result)
print(final)