from abc import abstractmethod #abc is "Abstract Base Class", a library which contains the infrastructure for abstract classes

class Bird:
    fly = True                 #in general birds fly

    def noise(self):           #in general birds make birdnoises
        print("Birdnoise")

    _babies = 0                 #unlike kangaskhan, birds aren't born with babies

    def reproduce(self):       #however, these birds reproduce asexually
        self.babies += 1    

    @abstractmethod            #birds have no general way of eating, this tells us
    def eat(self):             #we have to define each bird's eating method
        pass
    
    extinct = False            #generally birds are not extinct when discovered

class Owl(Bird):               #Owls are a type (subclass) of bird

    def reproduce(self):       #owls have more babies than general bird
        self.babies += 6       #This is "overiding" the reproduce method, using polymorphism
    
    def eat(self):             #owls eat by pecking, apparently
        print("Peck Peck")
    
class Dodo(Bird):
    Fly = False                #Override variables
    extinct = True

    def eat(self):
        print("Nom Nom")
    
    def reproduce(self):
        if not self.extinct:
            self.babies += 1
        else:
            print("No more dodos")

dead = Dodo()