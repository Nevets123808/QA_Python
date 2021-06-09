class students:
    class_ = "student"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def grade(self, grade1, grade2, grade3):
        print(sum([grade1,grade2,grade3])//3)

student = students("johnny drop tables","25")
student.grade(50,65,23)
print(getattr(student,"class_"))