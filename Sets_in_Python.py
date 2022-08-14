# Sets 
#sets cannot print repeated values
a = {2,3,4,5,6,2}
print(type(a))
print(a)

# Empty set 
b = set()
print(type(b))
# Adding values in empty set
b.add(3)
b.add(5)
b.add(5)  # set is collection of non repetied elements
b.add("raj") #set is contain strings
print(b)
print(len(b))
b.remove("raj")
print(b)
b.pop()  #rendom take element in the set and return in output    
print(b)
b.clear()  #become empty of given set
print(b)
