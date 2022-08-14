# Python functions by Rajkumar Jangid 

import os
theory ='''the indians are waste lot of time to 
read theory ,they can not fouces on practical'''
print(type(theory)) 
print(len(theory))  
print(theory.endswith("dsfjkdsfj"))
print(theory.endswith("practical"))
print(theory.count("t"))
print(theory.count("not"))
print(theory.capitalize()) # makes first character capital of first string
print(theory.find("they"))
print(theory.find("is"))
print(theory.replace("indians","Bhartiya"))
print(theory.replace("read","write"))
 
#  Escape Squence 
demo = "this is window\n this is two window\t yes"
print(demo)
  
# problem2
letter = '''Dear <|NAME|>
you are selected !
Date <|DATE|>'''
print(letter)
 name = input("Enter your Name\n")
 date = input("Enter Date\n")
 print(letter.replace("<|NAME|>","name"))
 

