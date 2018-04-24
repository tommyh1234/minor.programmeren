class House(object):
    x = None
    y = None
    height = None
    width = None
    minimumSpace = None
    priceIncrease = None
    space = None
    value = None
    area = None

    def __init__(self, area):
        self.area = area

    def surface(self):
        return self.width * self.height

    def check_validity(self):
        endX = self.x + self.width
        endY = self.y + self.height

        self.space = self.get_space()
        if self.space < self.minimumSpace:
            return False

        for i in range(self.x, endX):
            for j in range(self.y, endY):
                # if there's something that is not this house
                if (self.area[i][j] is not None
                        and self.area[i][j] is not self):
                    return False

        return True

    def get_space(self):
        space = 0
        x = self.x
        y = self.y
        while (self.area.grid[x][y] is None or self.area.grid[x][y] is self):
            if x < self.x + space:
                x += 1
            elif y < self.y + space:
                y += 1
                x = self.x - space
            else:
                space += 1
                x = self.x - space
                y = self.y - space

        return space

    def get_price(self):
        price = self.value * (1 + (self.space - self.minimumSpace)
                              / 2 * self.priceIncrease)
        return price
