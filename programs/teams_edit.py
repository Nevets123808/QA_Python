with open("C:\\Users\\Steven\\Documents\\QA\\QA_Python\\teams.txt", "r+") as file:
    lines = file.readlines()
    lines[0] = "This is a new line\n"
    file.seek(0)
    [file.write(line) for line in lines]
    file.seek(0)
    lines = file.readlines()
    print(lines)