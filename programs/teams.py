with open("C:\\Users\\Steven\\Documents\\QA\\QA_Python\\teams.txt","r") as file:
    first = file.readline()
    print(f"first team is {first}")
    [file.readline() for _ in range(2)]
    print(f"fourth team is {file.readline()}")