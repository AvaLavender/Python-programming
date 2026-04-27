num = int(input("Enter a number to check if armstrong number: "))

sum = 0
this = num
while this > 0:
    digit = this % 10
    sum += digit ** 3
    this //= 10

if num == sum:
    print(f"{num} is an armstrong number.") 
else:    print(f"{num} is not an armstrong number.")