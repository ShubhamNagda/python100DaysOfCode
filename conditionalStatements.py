age = int(input("Enter your age"))

if(age<18):
    print("you are child because your age is ",age)

elif(age>18):
    if(age<50):
        print("you are Young because your age is ", age)
    else:
        print("you age old person because your age is", age)
