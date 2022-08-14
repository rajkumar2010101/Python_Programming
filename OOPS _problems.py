# Program to store details of few programmers using class 
# class Programmer:
#     company = "Microsoft"
#     def __init__(self,name,product,age):
#         self.name = name
#         self.product = product
#         self.age = age

#     def getdetails(self):
#         print(f"The Name of the Programmer is {self.name}")
#         print(f"The Product Name is {self.product}")
#         print(f"The Age of the Programmer is {self.age}")

# raj = Programmer("Rajkuamr" , "MS Office" , "20")
# kumar = Programmer("Kumar","GitHub","23")
# raj.getdetails()
# kumar.getdetails()

# Program to display square , squareroot and cube of a number 
class Calculator:
    def __init__(self,num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def squareRoot(self):
        print(f"The value of {self.number} squareRoot is {self.number **3}")

    def cube(self):
        print(f"The value of {self.number} Cube is {self.number **0.5}")
raj = Calculator(5)
raj.square()
raj.squareRoot()
raj.cube()



