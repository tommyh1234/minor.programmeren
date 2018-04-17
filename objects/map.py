class Map:
    width = 320
    height = 360
    __grid = [[0 for x in range(width)] for y in range(height)]
    __mansionList = []
    __bungalowList = []
    __familyHomeList = []

    def place_house(self, house, x, y):
        if house.check_validity(self):
            self.__grid[x][y] = house
            house.x = x
            house.y = y
            self.__mansionList.append(house)

    def check_house_balance(self):
        return 1
