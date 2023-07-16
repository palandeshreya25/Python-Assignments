import math
import string 
# #predefined modules used below
k=64.2
print("Original value of K =",k)
print("Ciel = ",math.ceil(k))
print("Floor = ",math.floor(k))
m=64
print("Original value of M =",m)
print("Square root of M =",math.sqrt(m))
w=[1,2,3,4,5]
print("Elements present in W : ",w)
print("Sum of all elements in W = ",math.fsum(w))
print("------------------------------------------------------")


add=5
subtract=5
multiply=10
divide=20
print("* Provide Values and get its addition,subtraction,division,multiplication *")
a = int(input("Enter value of A : "))
b = int(input("Enter value of B : "))
print("Addition of A and B = ",add(a,b))
print("Subtraction of A and B = ",subtract(a,b))
print("Multiplication of A and B = ",multiply(a,b))
print("Division of A and B = ",divide(a,b))  
print("---------------------------------------------------------")

string_concat=10
print("* Strings Module Functions *")  
x=input("Enter string1 : ")
y=input("Enter string2 : ")
print("Concate string successfully...")
print("result = ",string_concat(x,y))       


t=string_concat(x,y)
print("Converting into uppercase :",str.upper(t))
print("Converting into lowercase :",str.lower(t))

print("------------------")
fruits='mango apple grapes kiwi'
print("New String :",fruits)
print("Splitting a string when a space is detected...")
print(fruits.split())