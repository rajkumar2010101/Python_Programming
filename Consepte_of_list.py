# Create a list []

a = [3,3,4,53,53]
print(a)
print(a[3])
# change a list 
a[2] = 34
print(a)
 
# List with different data types 
li = [3,"raj",True,34.3,4]
print(li)
#  Access data mumbers usring index 
print(li[3])
print(li[2])
print(li[1])

# List slicing 
friends =["raj","ankur","jay","ram",34]
print(friends[0:3])
print(friends[2:4])

# List Method 
# Sorting 
l1 =[1,2,4,0,45,32,12,4,32,54]
print(l1)
l1.sort()
print(l1)

# Reverse the list 
l1.reverse()
print(l1)

# adds at the end of the list 
l1.append(34)
print(l1)
l1.append(32)
print(l1)

# insert function 
l1.insert(3,99)
print(l1)

# Pop in list 
l1.pop(4) #removes elements at index 4
print(l1)
l1.remove(99)
print(l1)

# Tupes
# Can not change tupes table 
t =(1,3,45,6,1,1)
t1 = () #empty tuple
t2 =(3,) #single element tuple
print(t[3])
print(t2)
print(t.count(1)) #Tuple method using count used for count 
print(t.index(45)) #used for find index value

# Create list for fruits 
fruits =["apple","banana","Grapes","mango","papaya","chiku","gavava"]
print(fruits)
print("most likely fruit is")
print(fruits[3])
print("Healthy fruits is ")
print(fruits[0:5])

#  6 Studends marks
st1 =[2,23,65,345,46,23,42,32,45] 
st2 =[2,23,43,35,46,5,434,32,45]
st3 =[2,23,4,35,456,5,42,32,45]
st4 =[2,23,43,35,46,5,434,32,45]
st5 =[2,23,4,35,46,5,42,32,45]
st6 =[2,23,4,35,434,545,4354,45,34]
print(st1)
print("sorted marks of student 1")
st1.sort()
print(st1)
print(st2)
print("sorted marks of student 2")
st2.sort()
print(st2)
print(st3)
print("sorted marks of student 3")
st3.sort()
print(st3)
print(st4)
print("sorted marks of student 4")
st4.sort()
print(st4)
print(st5)
print("sorted marks of student 5")
st5.sort()
print(st5)
print(st6)
print("sorted marks of student 6")
st6.sort()
print(st6)

# Program for sum a number in a list 
demo = [2,3,4,5]
print(demo[0] +4)
print(demo[1] +4)
print(demo[2] +4)
print(demo[3] +4)

# Count number of zero in a list 
zero = (7,0,8,0,9,0)
print(zero)
print("number of zeros in list",zero.count(0))