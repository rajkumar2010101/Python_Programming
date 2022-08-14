# Progrma to display sum of two number using OOP consept 
class Number:
     def sum(self):
         return self.a + self.b

 num = Number()
 num.a = 12
 num.b = 34
 s = num.sum()
 print(s)

# Program of Railway form 
 class RailwayFrom:
     fromType = "RailwayFrom"
     def printData(self):
         print(f"Name is {self.name}")
         print(f"Train is  {self.train}")
 rajApplication = RailwayFrom()
 rajApplication.name = "Rajkuamr"
 rajApplication.train = "Garibrath Express"
 rajApplication.printData()

# Program to implement a game 
 class Remote():
     pass
 class Player:
     def moveRigh(self):
         pass
     def moveLeft(self):
         pass
     def moveTop(self):
         pass
 remote1 = Remote()
 player1 = Player()
 if(remote1.isLeftPressed()):
     player1.moveLeft()

 #Progrma to display class attribute of employee 
 class Employee:
     company = "Google"
 raj = Employee()
 kumar = Employee()
 print(raj.company)
 p = kumar.company
 print(p)
 Employee.company = "Microsoft"
 print(raj.company)
 print(kumar.company)

 #Program to display instance attribute (First prefence of instance attribute)
  class Employee:
     company = "Google"
     salary = 100
 raj = Employee()
 kumar = Employee()
 raj.salary = 300
 kumar.salary = 400
 print(raj.salary)
 print(kumar.salary)

# Program for understand self parameter 
 class Employee:
     company = "Google"
     def getsalary(self):
         print("Salary is 100k")
 raj = Employee()
 raj.getsalary()
 print(raj.company)

# Progrma for static method 
 class Demo:
     company = "Google"
    
     def getsalary(self , signature):
         print(f"Salary is {self.salary} and Company is {self.company}\n{signature} ")

     @staticmethod
     def greet():   # static method is remove self keyword 
         print("Good Morning, sir")

 raj = Demo()
 print(raj.company)
 raj.salary = 10000
 raj.getsalary("Thanks!")
 raj.greet()

# Program for __init__ constructor 
class Jay:
    def __init__(self,name,salary,subunit):
        self.name = "Raj"
        self.salary = 100
        self.subunit = "YouTube"
        print("This is __init__ constructor , automatically exectue this fuction when object intilize")

    def getdetail(self):
        print(f"The Name of Employee is {self.name}")
        print(f"The Salary of Employee is {self.salary} ")
        print(f"The Subunit of Employee is {self.subunit} ")

raj = Jay("Raj",100,"YouTube")
raj.getdetail()
