class Cat:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"i am a cat. my name is {self.name} and my age is {self.age}")

    def make_sound(self):
        print("meowww")

class Dog:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"i am a dog. my name is {self.name} and my age is {self.age}")

    def make_sound(self):
        print("Barkkk")

c1 = Cat("Dudu", 2.5)
d1 = Dog("Kuku", 7)

for animal in (c1,d1):
    animal.make_sound()
    animal.info()