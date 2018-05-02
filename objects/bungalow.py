from objects.house import House


class Bungalow(House):
    height = 20
    width = 15
    minimumSpace = 6
    priceIncrease = 0.04
    value = 399000

    def __repr__(self):
        return ("{}".format(self.__class__.__name__))
