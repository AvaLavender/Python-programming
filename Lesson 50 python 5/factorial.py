def r_f(n):
    if n == 1:
        return n
    else:
        return n*r_f(n-1)
    
num = int(input("Enter number: "))

if num< 0:
    print("Sorry, factorial numbers does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print(f"the factorial of {num} is {r_f(num)}")