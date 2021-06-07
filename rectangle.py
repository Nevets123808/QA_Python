class rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def area(self):
        return self.height*self.width

rect = rectangle(10,4)
print (rect.area())