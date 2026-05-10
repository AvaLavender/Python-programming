class Computer:

    def __init__ (self):
        self.__maxprice = 200

    def sell(self):
        print('Selling price is {}'.format(self.__maxprice))

    def setMP(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

c.__maxprice = 1000
c.sell()

c.setMP(1000)
c.sell()