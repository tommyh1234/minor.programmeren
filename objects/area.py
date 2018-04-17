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
        if house.check_validity(self):
            for i in range(x, x + house.width):
                for j in range(y, y + house.height):
                    self.grid[i][j] = house
            self.mansionList.append(house)
        else:
            house.x = None
            house.y = None

    def check_house_balance(self):
        return 1
