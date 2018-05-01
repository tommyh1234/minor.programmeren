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
                if (self.area.grid[i][j] is not None
                        and self.area.grid[i][j] is not self):
                    return False

        return True

    def get_space(self):
        space = 0
        x = self.x
        y = self.y
        # when a given position is not taken by something else
        while (self.area.grid[x][y] is None or self.area.grid[x][y] is self):
            # check the next x pos within area
            if (x < self.x + self.width - 1 + space and
                    x >= 0 and x < self.area.width - 1):
                x += 1
            # check next y within area and reset x
            elif (y < self.y + self.height - 1 + space and
                  y >= 0 and y < self.area.height - 1):
                y += 1
                x = self.x - space
                # make sure x and y won't be out of area
                if x < 0:
                    x = 0
                if x > self.area.width - 1:
                    x = self.area.width - 1
                if y > self.area.height - 1:
                    y = self.area.height - 1

            elif (self.width + space < self.area.width or
                  self.height + space < self.area.height):
                # reset and check a larger area
                space += 1
                x = self.x - space
                y = self.y - space
                # make sure x & y won't be out of area
                if x < 0:
                    x = 0
                if x > self.area.width - 1:
                    x = self.area.width - 1

                if y < 0:
                    y = 0
                if y > self.area.height - 1:
                    y = self.area.height - 1
            else:
                break

        return space

    def get_price(self):
        price = self.value * (1 + (self.space - self.minimumSpace)
                              / 2 * self.priceIncrease)
        return price
