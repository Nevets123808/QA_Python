def numWord(n):
    magnitude = ["thousand","million","billion","trillion"]
    units =["","one","two","three","four","five","six","seven","eight","nine"]
    teens =["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    tens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

    numStr = str(n)
    hundInd = n//100 - 10*(n//1000)
    tenInd = n//10 - 10*(n//100)
    unitInd = n - 10*(n//10)
    if len(numStr) == 1:
        if n == 0:
            return "zero"
        else:
            return units[n]
    elif len(numStr) ==2:
        if n < 20:
            return teens[unitInd]
        if unitInd == 0:
            return f"{tens[tenInd]}"
        return f"{tens[tenInd]} {units[unitInd]}"
    elif len(numStr) ==3:
        return f"{units[hundInd]} hundred and {numWord(tenInd*10+unitInd)}"
    elif len(numStr) >=15:
        return "number out of range"
    elif len(numStr) >3:
        print("Hello")
        if len(numStr)%3 == 0:
            firstString = numStr[:3]
            secondString = numStr[3:]
        else:
            firstString = numStr[:len(numStr)%3]
            print(firstString)
            secondString = numStr[len(numStr)%3:]
        firstInt = int(firstString)
        secondInt = int(secondString)
        return f"{numWord(firstInt)} {magnitude[(len(numStr)//3)-1]}, {numWord(secondInt)}"


print(numWord(2249905467))
