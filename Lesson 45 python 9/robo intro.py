class Robot:

    species = 'robot'

    def __init__(self,name,age):
        self.name = name
        self.age = age
blu = Robot ('Blu', 10)

print('Blu is a {}'.format(blu.species))


print("{} is {} years old".format( blu.name, blu.age))
