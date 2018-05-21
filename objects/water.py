class Water(object):
    x = None
    y = None
    height = None
    width = None
    value = None
    area = None

    def __init__(self, area):
        self.area = area

    def surface(self):
        return self.width * self.height

    def check_validity(self):
        endX = self.x + self.width
        endY = self.y + self.height

        for i in range(self.x, endX):
            for j in range(self.y, endY):
                # if there's something that is not this water
                if (self.area.grid[i][j] is not None
                        and self.area.grid[i][j] is not self):
                    return False

        return True
