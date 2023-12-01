a = int(input("Enter first value"))
b = input("operation")
c = int(input("2nd Value"))

if b =='+':
    print(a+c)
elif b == '-':
    print(a-c)
elif b == '*':
    print(a*c)
elif b == '/':
    if c ==0:
        print("Error Divide by zero")
    else:
        print(a*c)
elif b == '%':
        print(a%c)
else:
    print("Error")
