# Author: Rajkumar
import os 
print(os.listdir())
a = "rajkumar"
b = 34
c = 34.34
print(a)
print(b)
print(c)
d = '''rajkumar is good '''
print(d)
p = True
print(p)
print(type(a))
print(type(p))
print(type(c))
print("The value is a+b",34-43.3)
# Assignment Operators
b /= 4
b += 4
print(b)

# Comparison Operator
b =(23>4)
print(b)
c =(34>=45)
print(c)
p = (34!=34)
print(p)

# Logical Operator 
co1 = True
co2 = False
print("The value of co1 and co2:",co1 and co2)

print("The value of co1 and co2:",co1 or co2)

print("The value of not co2 is:",not co2)
 
#  typecasting
a = "345"
a = int(a)
print(type(a))
print(a+54)

# input fuction 
a = input("Enter your name :")
a = int(a)  #convert a to an Integer 
print(type(a))