class House:
    x = 0
    y = 0
    height = 0
    width = 0
    minimumSpace = 0
    priceIncrease = 0
    value = 0

    def surface(self):
        return self.width * self.height

    def check_validity(self, map):
        return True

    def check_price(self, map):
        return 0
