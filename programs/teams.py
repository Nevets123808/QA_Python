teams =["Middenland", "Nuln", "Altdorf", "Kiev", "Skavenblight"]
with open("C:\\Users\\Steven\\Documents\\QA\\QA_Python\\teams.txt","w") as file:
    [file.write(team+"\n") for team in teams]

with open("C:\\Users\\Steven\\Documents\\QA\\QA_Python\\teams.txt","r") as file:
    lines_read= [0,3]
    [print(line) for index, line in enumerate(file) if index in lines_read]
    