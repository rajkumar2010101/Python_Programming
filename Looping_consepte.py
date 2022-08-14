# Program Demo 
j = 0
while j < 10:
    print("Yes" , str(j))
    j = j+1
    print("Done")

# Progrma Demo 2 
veg = ["Brinja","onion","potato","ginger"]
i = 0
while i <= len(veg):
    print(veg[i-1])
    i = i + 1

# Progrma 2 using for loop 
veg = ["Brinja","onion","potato","ginger"]
for item in veg :
    print(item)

# Program 3 
for n in range(8,13,2):
    print(n)
else :   #Optional
    print("This is inside else of for")

# Program 4 (for loop with break)
for n in range(2,30):
    print(n)
    if n == 20:
        break

# Program 4(for loop with continue )
for n in range(1,20):
    if n == 10:
        continue  #continue is a keyword , in program it skip 10 and print all number
    print(n)
        
# pass keyword 
def run(player):
    pass
i = 0
while i < 10:
    pass
for n in range(1,3):
    pass
print("Hello")

'''                            important programs                    '''
   
# Program to display given number of table 
a = int(input("Enter number: "))
for n in range(1,11):
    table = a * n 
    print(table)

# Abvoe program using while loop 
a = int(input("Enter Number : "))
i = 1;
while i <= 10 :
    table = a * i
    i = i  +  1
    print(table)

# Program to print star pattern  
a = int(input("Enter Number :"))
for n in range(1 , a):
     print("*"* (n+1))

# Program to print display star pattern  
a = int(input("Enter Number: "))
for i in range(1,a+1):
    print(" " *(a-i-1) , end="")
    print("*" *(2*i+1) , end="")
    print(" " *(a-i-1))
    

# Program to find that given number is prime or not 
a = int(input("Enter Number : "))
prime = True
for n in range(2,a):
    if(a % n) == 0:
        prime = False
        break
if prime:
    print("It is prime Number")
else:
    print("It is not prime number")

# Program 
l1  =  ["raj","sachin","rahul","sohan"]
for name in l1:
    if name.startswith("s"):
      print("Hello " + name)

# Program to find factorial of given number  
n! = 1*2*3*4.......*n 
num = int(input("Enter Number: "))
fact = 1
for i in range(1,num+1):
    fact = fact * i
print(f"The factorial of {num} is {fact}")
    
# Program to print natural number 

num = int(input("Enter Number: "))
sum = 0
for n in range(1,num+1):
    sum = sum + n 
print(f"The Sum of statring {num} natural Number is : {sum}")

# Program to print mutliplication table in reverse order 
a = int(input("Enter Number: "))
i = a
while i <= 10:
    m = a * i 
    i = i - 1
    print(f"Revers of {a} is : {m}")
