import random
from algorithms.randomalg import RandomAlgorithm
# from algorithms.speedrandom import SpeedRandomAlgorithm


class HillClimbingAlgorithm(object):
    def __init__(self, area, fhAmount, bAmount, mAmount):
        self.isDone = False
        self.tryCount = 0
        self.area = area
        # fill grid random
        self.randomAlg = RandomAlgorithm(self.area, fhAmount, bAmount, mAmount)
        while(self.randomAlg.isDone is False):
            self.randomAlg.execute()

        # make list of all houses
        self.houseList = []
        self.houseList.extend(self.area.mansionList)
        self.houseList.extend(self.area.familyHomeList)
        self.houseList.extend(self.area.bungalowList)

    def execute(self):

        while (len(self.area.mansionList)
               + len(self.area.familyHomeList)
               + len(self.area.bungalowList) != 60):
            break

        # total price grid
        currentTotalPrice = self.area.get_area_price()

        # pick random houses from list of placed houses
        currentHouse = random.choice(self.houseList)

        # save coordinates of current house
        backupX = currentHouse.x
        backupY = currentHouse.y
        print('Original location house: ({}, {})'
              .format(currentHouse.x, currentHouse.y))

        # random choice wich type of move: switch,
        # turn, move house in direction
        # randomTypeOfMove = random.randint(0,2)

        # # move house in a certain direction
        # if randomTypeOfMove == 0
        self.area.sliding_house(currentHouse, backupX, backupY)

        # if the price from the grid didn't increased
        # go back to orignal location
        newTotalPrice = self.area.get_area_price()

        # if randomTypeOfMove == 0
        if currentTotalPrice >= newTotalPrice:
            # remove house and place origanal house
            currentHouse.x = backupX
            currentHouse.y = backupY

            # place orignal house back
            self.area.place_house(currentHouse,
                                  currentHouse.x,
                                  currentHouse.y)
        self.tryCount += 1
        print("trycount {}".format(self.tryCount))

        if self.tryCount > 100:
            self.isDone = True

        print(currentTotalPrice)
        print("-------------------- ")
