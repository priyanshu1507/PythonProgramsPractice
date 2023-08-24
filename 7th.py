num = int(input("Enter the number you want to reverse"))
y = 0
while (num!=0):
    j = num%10
    num = num//10
    y = y*10
    y = y + j
print(y)

