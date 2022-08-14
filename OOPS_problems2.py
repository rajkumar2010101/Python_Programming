# Program to display problem solutions 
# will change the class attribute and object attribute 
# Answer is that it does't change class attribute by instance  
class Sample:
    a = "Harry"         #This is class attribute
obj = Sample()      
obj.a = "Rajkumar"      #This is set instanse attribute
print(Sample.a)
print(obj.a)

# Progrma to implement static method in problem calculator 
class Calculator:
    def __init__(self,num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def squareRoot(self):
        print(f"The value of {self.number} squareRoot is {self.number **3}")

    def cube(self):
        print(f"The value of {self.number} Cube is {self.number **0.5}")
    
    @staticmethod
    def greet():
        print("***Hello there welcome to best calculator of the word***")

raj = Calculator(5)
raj.greet()
raj.square()
raj.squareRoot()
raj.cube()

# Program to change self parameter by other parameter 
class Sample:
    def __init__(raj , name):  #You can replace self paremeter by other paremeter
        raj.name = name 

obj = Sample("Rajkumar")
print(obj.name)

