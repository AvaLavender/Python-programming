x = int(input("Enter Value of x:"))
y = int(input("Enter Value of y:"))
z = int(input("Enter Value of z:"))

temp = x
x = y
y = z
z = temp

print("value of x after swapping", x)
print("value of y after swapping", y)
print("value of z after swapping", z)   