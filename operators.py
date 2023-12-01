# ---------------Arithmetic Operator --------------
print("Arithmetic Operator")
a=10
b=5

print(a+b) #addition
print(a-b) #subtraction
print(a*b) #Multiplication
print(a/b) #Division 
print(a%b) #Modulus                
print(a//b) #Floor division        only intger no. means 2.0 => 2
print(a**b) #Exponentiation        10*10*10*10*10


# -------------Assignment Operator -------------------
print("\n Assignment Operator")
c = 15

d = c # is equal to
print(d) 

c += c # c = c+c
print(c)

c -= c # c = c-c
print(c)

c = 15
c *= c # c = c*c
print(c)

c /=c # c= c/c
print(c)

c %=c # c= c%c
print(c)

c=15
c **= 2 # c = c**2
print(c)

c=15
c //= c # c= c//c
print(c)


# -------------Comparision Operator -------------------
print("\n Comparision Operator")

z =10
y = 20

print("is z equal to y" , z==y)
print("is Not Equal to y", z!=y)
print("is z less and equal to y" , z<=y)
print("is z greater and equal to y" ,z>=y)
print("is z less than  y" ,z<y)
print("is z greater y", z>y )


#-----------------Logical Operator-------------------------
print("\n Logical Operator")

w = 5
x = 9

print(w<x and w>x) #Returns True if both statements are true 
print(w<x or w>x)  #Returns True if one of the statements is true 
print(not(w>x))    #Reverse the result, returns False if the result is true 


# -----------------Identity Operators-----------------------
print("Identity Operators ") 

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # returns True because z is the same object as x

print(x is y) # returns False because x is not the same object as y, even if they have the same content

print(x is not z) # returns False because z is the same object as x

print(x is not y) # returns True because x is not the same object as y, even if they have the same content


# -----------------Membership Operators-----------------------
print("Membership Operators") 

p = ["apple", "banana"]

print("banana" in p) # returns True because a sequence with the value "banana" is in the list

print("banana" not in p) # returns False because a sequence with the value "banana" is in the list
