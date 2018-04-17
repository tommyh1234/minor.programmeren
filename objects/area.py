class Area:
    width = 320
    height = 360
    grid = [[None for x in range(width)] for y in range(height)]
    mansionList = []
    bungalowList = []
    familyHomeList = []

    def place_house(self, house, x, y):
        house.x = x
        house.y = y
        if self.check_validity(house):
            for i in range(x, x + house.width):
                for j in range(y, y + house.height):
                    self.grid[i][j] = house
            self.mansionList.append(house)
        else:
            house.x = None
            house.y = None

    def check_validity(self, house):
        endX = house.x + house.width
        endY = house.y + house.height

        for i in range(house.x, endX):
            for j in range(house.y, endY):
                # if there's something that is not this house
                if (self.grid[i][j] is not None
                        and self.grid[i][j] is not house):
                    return False

        return True

    def check_house_balance(self):
        return 1
