def add(a,b):
    c=a+b
    print(c)
def sub(a,b):
    c = a- b
    print(c)
def mul(a,b):
    c = a*b
    print(c)
def div(a,b):
    if (a>b):
        c= a/b
    else:
        c = b/a
    print(c)

x = int(input("Enter First Number"))
y = int(input("Enter Second Number"))

cal = str(input("Enter The Operation You want to perform. +,-,/,*    "))

if (cal.__contains__("+")) :
    add(x,y)
elif (cal.__contains__("-")):
    sub(x,y)
elif (cal.__contains__("*")):
    mul(x,y)
elif (cal.__contains__("/")):
    div(x,y)
else: print("Please Enter Valid Operation")