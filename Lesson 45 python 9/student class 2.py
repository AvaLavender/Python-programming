class student:
    grade=10
    name = "Ava"

    def intro(self):
        print('Hai im a student')

    def info(self):
        print('I am ', self.name)
        print('I study in class ', self.grade)
ob = student()
ob.intro()
ob.info()
