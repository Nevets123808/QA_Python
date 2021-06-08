def numWord(n):
    #orders_of_magnitude = ["","hundred","thousand","million","billion","trillion"]
    units =["","one","two","three","four","five","six","seven","eight","nine"]
    #teens =["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    if len(str(n)) == 1:
        if n == 0:
            return "zero"
        else:
            return units[n]
    elif len(str(n)) ==2:
        return f"{tens[n//10]} {units[n-10*(n//10)]}"

for number in range(100):
    print(numWord(number))
