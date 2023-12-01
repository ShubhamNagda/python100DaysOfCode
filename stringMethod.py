# Strings are immutable

name ="shubham-$$$$-shubham"

print(len(name))  #length of string

print(name.upper())  #change strings into uppercase
print(name.lower())  #change strings into lowercase

print(name.rstrip("$"))  # not show $ from string 

print(name.replace("shubham","umesh"))  #change all shubham into umesh in string

print(name.split("-"))  # create list where - is present

blog = "introduction To python python Is bEst prograMming language"
print(blog.capitalize())  # create first latter into capital and all into lowercase

print(blog.center(50))  # center all string with 50 space from both(left right) sides

print(blog.count("python")) # count how many times python repeat in string blog

print(blog.endswith("language")) # is return true if string end with language
print(blog.endswith("To" , 2,15)) # is return true if letter "To" end with 15th index

print(blog.find("Is")) # show index where "is" is started or -1 if "is" is not in string
# print(blog.index("Ishhh")) # similar as find but not renturn -1 if Ishhh is not in string

str1 = "WelcomeToTheConsole"
print(str1.isalnum())  # if str1 is alfanumeric return true otherwise false a-z,A-Z,0-9
str1 = "Welcome"
print(str1.isalpha()) # if str1 is alfa return true otherwise false a-z,A-Z

str1 = "hello world"
print(str1.islower()) #return true if all words are lower case

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())  #return true if string is printable 
str1 = "         "       #using Spacebar
print(str1.isspace()) #return true if string has sapce
str2 = "  "       #using Tab
print(str2.isspace()) # return true if string has sapce

str1 = "World Health Organization" 
print(str1.istitle()) #return true if all word starts with uppercase

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python")) #return true if string starts with python

str1 = "Python is a Interpreted Language" 
print(str1.swapcase()) # swap lowercase into uppercase and uppercase into lowercase

str1 = "His name is Dan. Dan is an honest man."
print(str1.title()) #convert str1 into title
