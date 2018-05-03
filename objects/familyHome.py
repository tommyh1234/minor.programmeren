from objects.house import House


class FamilyHome(House):
    height = 16
    width = 16
    minimumSpace = 4
    priceIncrease = 0.03
    value = 285000

    # def __repr__(self):
    #     return ("{}".format(self.__class__.__name__))
