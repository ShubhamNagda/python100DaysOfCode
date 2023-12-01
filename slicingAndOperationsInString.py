# < ----------------------- Slicing in python ----------------------------------->

name = "Shubham nagda"

print(name[0:8])   #print 0 to n-1 
# output is shubham

# <--------------------------length of string ----------------------------------->

fruit = "mango"
len1 = len(fruit)  #length of mango

print(fruit ,"is a", len1, "letter word.")

print(fruit[0:-3]) # it mean => (fruit[0:len(fruit)-3]) 👇👇
print(fruit[0:len(fruit)-3])

print(fruit[len(fruit)-3:len(fruit)-1])

