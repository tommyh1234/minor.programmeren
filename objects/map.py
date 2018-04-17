class Map:
    width = 320
    height = 360
    grid = [[0 for x in range(width)] for y in range(height)]
    list = []

    def place_house(self, house, x, y):
        if house.check_validity(self):
            self.grid[x][y] = house
            list.append(house)

    def check_house_balance(self):
        return 1
