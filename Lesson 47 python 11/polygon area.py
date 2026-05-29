class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side 
        
    def area(self):
        return self.side * self.side
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return self.base * self.height / 2
    
while True:
    print("Enter your choice to continue")
    print('1. Area of a square')
    print('2. Area of a rectangle')
    print('3. Area of a triangle')
    u_c = input()
    if u_c not in ['1','2','3']:
        print("Please enter a valid option")
        continue
    elif u_c == '1':
        side = int(input("Enter the side of the square: "))
        s = Square(side)
        print(f"The area of the square is {s.area()}")
    elif u_c == '2':
        length = int(input("Enter the length of the rectangle: "))
        width = int(input("Enter the width of the rectangle: "))
        r = Rectangle(length, width)
        print(f"The area of the rectangle is {r.area()}")
    elif u_c == '3':
        base = int(input("Enter the base of the triangle: "))
        height = int(input("Enter the height of the triangle: "))
        t = Triangle(base, height)
        print(f"The area of the triangle is {t.area()}")

    
