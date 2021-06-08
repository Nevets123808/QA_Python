number = int(input("Please enter a number: "))

#print y = m*x for 0<x<=number, and 0<m<=numer
for x in range(1,number+1):
    for m in range(1,number+1):
        print(m*x,end = "   ")
    print()