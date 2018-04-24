class Area(object):
    width = 320
    height = 360
    grid = [[None for x in range(width)] for y in range(height)]
    mansionList = []
    bungalowList = []
    familyHomeList = []

    def place_house(self, house, x, y):
        house.x = x
        house.y = y
        kind = type(house).__name__
        if house.check_validity():
            for i in range(x, x + house.width):
                for j in range(y, y + house.height):
                    self.grid[i][j] = house
            if kind == "Mansion":
                self.mansionList.append(house)
            elif kind == "Bungalow":
                self.bungalowList.append(house)
            elif kind == "FamilyHome":
                self.familyHomeList.append(house)

    def check_house_balance(self):
        mansions = len(self.mansionList)
        bungalows = len(self.bungalowList)
        familyHomes = len(self.familyHomeList)
        total = mansions + bungalows + familyHomes

        if mansions / total * 100 != 15:
            return False
        if bungalows / total * 100 != 25:
            return False
        if familyHomes / total * 100 != 60:
            return False
        return True

    def count_grid_price(self):

        totalPriceGrid = 0

        while i < len(mansionList)
            totalPrice +=  mansionList[i].get_price()
            i += 1
        while i < len(bungalowList)
            totalPrice +=  bungalowList[i].get_price()
            i += 1
        while i < len(familyHomeList)
            totalPrice +=  familyHomeList[i].get_price()
            i += 1
        return totalPriceGrid



