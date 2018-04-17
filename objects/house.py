class House(object):
    x = None
    y = None
    height = 0
    width = 0
    minimumSpace = 0
    priceIncrease = 0
    space = 0
    value = 0

    def __init__(self, space):
        self.space = space
        self.width = self.width + space * 2
        self.height = self.height + space * 2

    def surface(self):
        return self.width * self.height

    def get_price(self, area):
        price = self.value * (1 + (self.space - self.minimumSpace)
                              / 2 * self.priceIncrease)
        return price
