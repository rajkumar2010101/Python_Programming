# Avarage of three numbers 
import os
a = input("first no :")
b = input("second no :")
c = input("Third no :")
a = int(a)
b = int(b)
c = int(c)
print(type(a))
print(type(b))
print(type(c))
avg = (a+b+c)/3
print("Avarage of three numbers :" ,avg)

# Division 
p = a / b
print("Answer of division of a and b :",p)

# Comparison of Two numbers 
p = (a > b)
print("Grater number is using boolean from a and b1:",p)

# Squrae of number 
i = input("Given Number :")
i = int(i)
a = int(i)
g = i * i 
print("Square is :",g)

# Remainder
print("Remainder of a and b is :",a%b) 

# Strings operation 
hi = "hello, "
by = 'Rajkumar'
c = hi + by
print(c)
print(hi + by)
print(type(hi))
print(type(by))

# String slicing 
name = "rajkumar"
print(name[3])
print(by[0])
print(name[0:4])
print(hi[1:3])
c = name[-2:-4]
print(c)
name1 = "Rajkumarisgood"
 d = name1[0::3]     # 3 is show the differnce between string 
print(d)

