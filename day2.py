# Arithmetic Operators
a =  int(input ("Enter number 1:"))
b =  int(input ("Enter number 2:"))
sum=a+b
sub=a-b
mul=a*b
div=a/b
div2=a//b
mod=a%b
expo=a**b
print (f"The Addition of {a} and {b} is {sum}")
print (f"The Subtraction of {a} and {b} is {sub}")
print (f"The Multiplication of {a} and {b} is {mul}")
print (f"The Division of {a} and {b} is {div}")
print (f"The division of {a} nd {b} is {div2} ")
print (f"The Modulus of {a} and {b} is {mod}")
print (f"The Exponent of {a} and {b} is {expo}")


#Assignment operator
a=10
b=20
c=30
a+=b 
c-=b 
print(a)
print(c)


# Comparision Operators
a =  int(input ("Enter number 1:"))
b =  int(input ("Enter number 2:"))
#equal to  
if(a==b):
    print ("True")
else:
    print ("False")
#not equal to
if(a!=b):
    print ("True")
else:
    print ("False")
#greater than
if (a>b):
    print("True")
else:
    print("False")
#less than
if (a<b):
    print("True")
else:
    print("False")


#Logical Operators
a =  int(input ("Enter number 1:"))
b =  int(input ("Enter number 2:"))
print ((a>2)and (b>=6))
print ((a>2) or (b>=6))
print ( not True)


#Bitwise Operators
a =  int(input ("Enter number 1:"))
b =  int(input ("Enter number 2:"))
print(a>>1)
print(a<<2)
print (a&b)
print (a|b)
print (a^b)


#Identity operator
a =  int(input ("Enter number 1:"))
b =  int(input ("Enter number 2:"))
print(a is not b)
print(a is b)


#Membership operator
a =  str(input ("Enter String:"))
print('s' in a)
print ('P' in a)


#char to ASCII
#a="A"
#val=ord(a)
#print(val)

#ASCII to char
#print(chr(0))

#string formatting
#a=10
#b=20
#sum=a+b
#print("The addition of ",a," and ",b," is :",sum)
#print ("The addition of {} and {} is {}".format(a,b,sum))
#print(f"The addition of {a} and {b} is {sum}")
#print("The addition of %d and %d is %d"%(a,b,sum))

#positive negative
# a=int(input("Enter the number:"))
# if a>0:
#     print ("+ve")
# elif a<0:
#     print ("-ve")
# else:
#     print ("0")

#
# a=int(input("Enter num 1:"))
# b=int(input("Enter num 2:"))
# c=int(input("Enter num 3:"))
# if(a<c):
#     if (a<b):
#         print("a is smallest")
#     else:
#         print("b is smallest")
# else:
#     print ("c is smallest")

