class House(object):
    x = None
    y = None
    height = None
    width = None
    minimumSpace = None
    priceIncrease = None
    space = None
    value = None

    def __init__(self, space):
        self.space = space
        self.width = self.width + space * 2
        self.height = self.height + space * 2
        if space < self.minimumSpace:
            raise RuntimeError("The garden is too small!")

    def surface(self):
        return self.width * self.height

    def get_price(self, area):
        price = self.value * (1 + (self.space - self.minimumSpace)
                              / 2 * self.priceIncrease)
        return price
