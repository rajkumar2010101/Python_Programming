# Program to display age critiera 
a = input("Enter Age:")
a = int(a)
if(a > 18):
    print("You are eligible")
elif(a < 18):
    print("You are not eligible")
else :
    print("Take Pations")

# Program to display higest number from four enterd numbers 
a = int(input("Enter first number\n"))
b = int(input("Enter second number\n"))
c = int(input("Enter third number\n"))
d = int(input("Enter fourth number\n"))
if(a > b):
    print("Greater number is:",a)
elif(b > c):
    print("Greater number is:",b)
elif(c > d):
    print("Greater number is:", c)
else:
    print("Greater number is :",d)

'''Program to display total marks of student with three 
subject and passing critarea is 40% '''
import math
a = int(input("Enter marks of Maths:"))
b = int(input("Enter marks of physics:"))
c = int(input("Enter marks of chemistry:"))
total = a + b + c
percentage = total / 300 
final = percentage * 100
if(final >= 40):
    print("Student is pass")
elif( final == 33):
    print("Student get grees")
else:
    print("Student is Failed")

'''Progrm to illstrate the following string contain 10 charcter or less 
than 10 character '''
str10 = input("Enter any string: ")
if(len(str10) <=10):
    print("This is valid String ")
else :
    print("This is not valid String")

# Check the spam of perticular comment 
text = input("Enter your Text:")
if("make lot of money" in text): # "in" is keyword 
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False
if(spam == True):
    print("Text is Spam")
else:
    print("Text is not Spam")

# Check that given name by user is present in list or not 
lis = ["raj","vikas","rahul","ankur","rohan"]
take = input("Enter Names: ")
if take in lis :
    print("You are right given name in the list")
else:
    print("You are wrong because given name is not in list")


#Program to display grades behalf of marks
take = int(input("Enter your marks: "))
if take >= 90:
    grade = "A+"
elif take >= 80:
    grade = "A"
elif take >= 70:
    grade = "B"
elif take >= 60:
    grade = "C"
elif take >= 50:
    grade ="D"
else :
    grade ="F"
print("You get "+ grade)

# Check the given post has name 'raj' or not 
name = input("Enter search:\t")
if ("RAJ" in name):
    print("You are right")
elif ("Raj" in name):
    print("You are right")
elif ("RAj" in name):
    print("You are right")
elif ("raj" in name):
    print("You are right")
elif ("rAJ" in name):
    print("You are right")
elif ("raJ" in name):
    print("You are right")
elif ("rAj" in name):
    print("You are right")
elif ("RaJ" in name):
    print("You are right")
else :
    print("You are wrong ")
