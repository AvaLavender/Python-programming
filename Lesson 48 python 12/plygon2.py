class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side 
        
    def area(self):
        self.side = int(input("Enter the side of the square: ")) 
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, height, base):
        self.height = height
        self.base = base
        
    def area(self):
        self.height = int(input("Enter the height of the triangle: "))
        self.base = int(input("Enter the base of the triangle: "))
        return self.base * self.height / 2
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        self.length = int(input("Enter the length of the rectangle: "))
        self.width = int(input("Enter the width of the rectangle: "))
        return self.length * self.width
    
s = Square(input)
t = Triangle(input, input)  
r = Rectangle(input, input)
    
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
        s.area()
    elif u_c == '2':
       r.area()
    else:
        t.area()

