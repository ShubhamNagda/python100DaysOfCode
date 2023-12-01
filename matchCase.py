a = int(input("print Your age: "))

match a:
    case 0 :
        print("please be born first")
    case 80:
        print("Please do not use the bike because you are an old person")
    case _ if(a>=18):   
        print("you can drive")
    case _ if(a<18):
        print("you can not drive")
    case _: #like default case in c++,java,c
        print("😒😒")