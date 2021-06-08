def numWord(n):
    #orders_of_magnitude = ["","hundred","thousand","million","billion","trillion"]
    units =["","one","two","three","four","five","six","seven","eight","nine"]
    teens =["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

    hundInd = n//100 - 10*(n//1000)
    tenInd = n//10 - 10*(n//100)
    unitInd = n - 10*(n//10)
    if len(str(n)) == 1:
        if n == 0:
            return "zero"
        else:
            return units[n]
    elif len(str(n)) ==2:
        if n < 20:
            return teens[unitInd]
        return f"{tens[tenInd]} {units[unitInd]}"
    elif len(str(n)) ==3:
        return f"{units[hundInd]} hundred and {numWord(tenInd*10+unitInd)}"
        

for number in range(100,1000):
    print(numWord(number))
