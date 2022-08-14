import os
a =input("first number:")
b =input("second number:")
a = int(a)
b = int(b)
print("Sum of two numbers:",a+b)
print(type(a))
print(type(b))

# Find Double space in a string 
print("Double Sapce Detection")
st = '''This is  a String  '''
doublespace = st.find("  ")
print(doublespace)

# Replace Double space to single space 
st1 = '''The earth is  unqiue in the galaxy  but it is  possible or  not'''
st1 = st1.replace("  "," ")
print(st1)

# using escape sequnce 
letter ='''Dear raj, This is very good! Thanks!'''
print(letter)
format ='''Dear raj\n\tThis is very good!\n\t\t\tThanks!'''
print(format)