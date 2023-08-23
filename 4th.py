x = int(input("Enter First Number"))
y = int(input("Enter 2nd Number"))
z = int(input("Enter 3rd Number"))

if (x>y) and (x>z):
    print(x,"is greatest")
elif (y>z) and (y>x):
    print(y,"is Greatest")
else: print(z,"is Greatest")
