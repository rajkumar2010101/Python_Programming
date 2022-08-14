# Program using funtion in python 
def percent(marks):
    return ((marks[0] + marks[1] + marks[2] + marks[3]) / 400) * 100

marks1 = [45,76,87,56]
percentage1 = percent(marks1)
marks2 = [56,7,68,76]
percentage2 = percent(marks2)
print(percentage1,percentage2)

# Program 
def greet(name):
    return print("Good Morning, "+name)
name1 = input("Enter Name: ")
greet(name1)

# Program to evaluate factaorial of given number using reccrusion 

# def fact(n):  #using function 
    f = 1
    for i in range(n):
        f = f * (i+1)
   return f
def fact_recc(n):   #using reccrusion
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact_recc(n-1)
# ff = fact(22)
ff = fact_recc(5)
print(ff)

'''                                      Important Programs                       '''
# Program to find gratest from threee numbers using functions 
def gret(a,b,c,d):
    if(a > b):
        print(a)
    elif(b > c):
        print(b)
    elif(c > d):
        print(c)
    else:
        print(d)
a1 = int(input("Enter first number: ")) 
b1 = int(input("Enter second number: "))
c1 = int(input("Enter third number: "))
d1 = int(input("Enter fourth number: ")) 
print("The Gratest Number is :") 
gret(a1,b1,c1,d1) 

# Program to convert celsius to fahernite using fuction 
def change(cel):
    s = 5*c
    F =( 9 / s) + 32
    return print(F)
c = int(input("Enter .C: "))
print("Fahernite is : ")
change(c)

# Program to sum of natural number using reccrsion 
def rec(n):
    if n == 0 :
       return 0
    elif n == 1:
       return 1
    else:
        return n + rec(n-1)
n = int(input("Enter Number: "))
b = rec(n)
print("Sum of given natural number: ",b)

# Program to print multipliction table of given number 
def mul(p):
   for i in range(1,11):
      r  = ( p * i )
      s = print(f"{p} X {i} = {r}")
a = int(input("Enter Number: "))
mul(a)

# Program 
print("Hello" , end=" ")
print("How are" , end=" ")
print("You are fine" , end=" ")
print("I am also fine" , end=" ")

# Program to print star pattern 
def star(n):
   for i in range(n):
      print("*"*(n-i)) # prints * n-1 times
b = int(input("Enter Number: "))
star(b)

# Program to remove word  in any string and strip that string 
def remove_and_split(string, word):
   newstr = string.replace(word,"Name")
   return newstr.strip()

this = '''       Rajkumar is a good     '''
b = remove_and_split(this ,"Rajkumar")
print(b)
