class Area(object):
    width = 320
    height = 360

    def __init__(self):
        self.grid = [[None for y in range(self.height)]
                     for x in range(self.width)]
        self.mansionList = []
        self.bungalowList = []
        self.familyHomeList = []

    def place_house(self, house, x, y):
        house.x = x
        house.y = y
        kind = type(house).__name__
        if house.check_validity():
            # place the house on every coordinate that is covered by the house
            for i in range(x, x + house.width):
                for j in range(y, y + house.height):
                    self.grid[i][j] = house
            # add the house to the appropriate list
            if kind == "Mansion":
                self.mansionList.append(house)
            elif kind == "Bungalow":
                self.bungalowList.append(house)
            elif kind == "FamilyHome":
                self.familyHomeList.append(house)
        else:
            raise RuntimeError("Cannot validly place \
                                house at these coordinates.")

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

    def get_area_price(self):

        totalPrice = 0
        i = 0

        while i < len(self.mansionList):
            self.mansionList[i].get_space()
            totalPrice += self.mansionList[i].get_price()
            i += 1
        while i < len(self.bungalowList):
            self.bungalowList[i].get_space()
            totalPrice += self.bungalowList[i].get_price()
            i += 1
        while i < len(self.familyHomeList):
            self.familyHomeList[i].get_space()
            totalPrice += self.familyHomeList[i].get_price()
            i += 1
        return totalPrice
