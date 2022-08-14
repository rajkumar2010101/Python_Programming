# #Dictionary drived 
md = {
    "Fast":"complate in few seconds",
    "raj":"A learner",
     "jay":"ram ram",
     "lis":[2,3,34,54],
     "nextmd":{"raj1":"is a good"}
}
# Dictionary Methods 
print(md.keys())         #print key values of dictionary
print(type(md.keys()))
print(list(md.keys()))
print(list(md.values()))   #print values of keys of dictionary
print(md.values()) 
print(md.items())   #print the(keys,values) contain of dictionary
'''Update contain of main dictionary by another dictionary'''
updatemd = {
   "Ankur":"is the best friend",
   "jay":"rajkumar" 
}     
md.update(updatemd)
print(md)
print(md["jay2"])            #throws an error as jay2 is not present in the dictionary
print(md.get("jay2"))        #Returns None as jay2 is not present in the dictionary



