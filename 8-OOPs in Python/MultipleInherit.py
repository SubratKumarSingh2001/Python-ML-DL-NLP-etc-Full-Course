class Animal :
    def __init__(self, name):
        self.name = name

    def speak(self) :
        print("Subclass must implement this method")

#Base Class:2
class Pet :
    def __init__(self, owner):
        self.owner = owner
    
    def petName(self) :
        print(f"The owner name is : {self.owner}")

#Derived Class
class Dog(Animal, Pet) : #Multiple inheritance 
    def __init__(self, name, owner, age):
        #if there is one parent class then it was easy to use the super() to inherit the properties
        #here we will use class name and constructor Animal.__init() so on
        Animal.__init__(self,name) #this will also inherit the instance methods
        Pet.__init__(self, owner) #this will also inherit the instance methods
        self.age = age
    
    def speak(self) :
        return f"{self.name} says woof"
    
    
    def dogAge(self) :
        return f"The age of {self.name} is : {self.age}"
    
dog1 = Dog('Sheru', 'Raj', 12)
print(dog1.dogAge())
print(dog1.speak())
print(dog1.name, dog1.owner)
dog1.petName()
dog1.speak() #it will print the Dog class speak() method overriding
        