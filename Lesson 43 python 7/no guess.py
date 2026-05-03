import random
x = random.randint(1, 100)
i = 5

y = int(input("Enter number to guess: "))

while y != x:

    if y < x:
        print('Oops, thats wrong. Try higher')
    if y > x:
        print("Oops, thats not right. Try lower")
    
    i = (i - 1)

    if i==0:
        print("Sorry, your chances are over. The number was: ", x)
        break 
    y = int(input("Enter number to guess: "))


if y == x :
    print('Yay, you are correct!')


    

         



