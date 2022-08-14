# First Problem 
from msilib import change_sequence


dis = {
    "savidhan":"constitue",
    "desh":"country",
    "vishvas":"Trust",
}
print("Options is :",dis.keys())
a = input("Enter the Hindi word\n")
print("The meaning of your  word is :",dis.get(a))
print(type(dis))

# Second problem 
f1 = int(input("enter first number:"))
f2 = int(input("enter second number:"))
f3 = int(input("enter third number:"))
f4 = int(input("enter four number:"))
f5 = int(input("enter five number:"))
# unique numbers using set
display = {f1,f2,f3,f4,f5}
print(display)
 
# Third problem 
s = {18,"18"}
print(s)

# four problem 
s = set()
print(len(s))
s.add(13)
print(len(s))
s.add(234)
print(len(s))
s.add("34")
print("The final set element is ",s)
print("Lenght of final set:",len(s))

# five problem 
dis = {}
a = input("Enter your fav. lang. vikas\n")
b = input("Enter yout fav. lang. rahul\n")
c = input("Enter your fav. lang. Ankur\n")
d = input("Enter your fav. lang. jay\n")
dis["Vikas"] = a
dis["Rahul"] = b
dis["ankur"] = c
dis['jay'] = d
print(dis)
print(type(dis))
# if two friends have same name

# six problem
simple = [2,3,4,"raj",[3,4]]
print(simple)
change_sequence in list
simple[0] = 34
simple[1] = 3
simple[2] = 35
simple[3] = "kumar"
simple[4][0] = 45
simple[4][1] = "jay"
print(simple)
