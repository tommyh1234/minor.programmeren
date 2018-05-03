import random
from algorithms.randomalg import RandomAlgorithm


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
        currentTotalPrice = self.area.get_area_price()
        # pick random houses from list of placed houses
        currentHouse = random.choice(self.houseList)

        print('CurrentHouse: {}'.format(currentHouse))

        # save cordination of house
        backupX = currentHouse.x
        backupY = currentHouse.y

        print('Original location: ({}, {})'
              .format(currentHouse.x, currentHouse.y))

        # remove current house from the map
        self.area.remove_house(currentHouse)

        # choose to move horizontal or vertical
        directionShift = random.randint(0, 1)
        print("Direction: {}".format(directionShift))

        # determine distance to shift the house with
        currentHouse = self.determineShift(currentHouse, directionShift)
        print(currentHouse)
        print("New location: ({}, {}).".format(currentHouse.x, currentHouse.y))
        print("House: {}".format(currentHouse))

        # place new house
        try:
            self.area.place_house(currentHouse, currentHouse.x, currentHouse.y)
        # replace with true/false for place house
        # include except RecursionError: place old house back.
        except RuntimeError:
            print("Trying to shift house to invalid location ({}, {}) "
                  "so revert to original position ({}, {})."
                  .format(currentHouse.x, currentHouse.y, backupX, backupY))

            # remove house and place origanal house
            currentHouse.x = backupX
            currentHouse.y = backupY

            # place new house
            print("Trying to place the house back to previous location")
            print(len(self.houseList))
            self.area.place_house(currentHouse, currentHouse.x, currentHouse.y)

        # check if value of grid is increased or stays the same
        newTotalPrice = self.area.get_area_price()

        if currentTotalPrice >= newTotalPrice:
            # remove house and place origanal house
            currentHouse.x = backupX
            currentHouse.y = backupY

            # place new house
            self.area.place_house(currentHouse,
                                  currentHouse.x,
                                  currentHouse.y)

        if self.tryCount > 100:
            self.isDone = True

        print("--------------------")

    # determine distance to shift the house with
    def determineShift(self, currentHouse, directionShift):
        # pick random distance to shift the house with
        amountShift = random.randint(-10, 10)
        print("amountShift: {}".format(amountShift))

        # change house in chosen direction,
        # but only if it still falls within the map TODO break maken
        if directionShift == 0:
            tempCurrentHouseX = currentHouse.x + amountShift
            tempBoundry = (self.area.width
                            - currentHouse.width
                            - currentHouse.minimumSpace)
            if (tempCurrentHouseX > currentHouse.minimumSpace and
                    tempCurrentHouseX < tempBoundry):
                currentHouse.x += amountShift
                return currentHouse
            else:
                print("AmountShift ({}) not possible "
                      "(house would be outside map)".format(amountShift))
                self.determineShift(currentHouse, directionShift)
        else:
            tempCurrentHouseY = currentHouse.y + amountShift
            tempBoundry = (self.area.height
                            - currentHouse.height
                            - currentHouse.minimumSpace)
            if (tempCurrentHouseY > currentHouse.minimumSpace and
                    tempCurrentHouseY < tempBoundry):
                currentHouse.y += amountShift
                return currentHouse
            else:
                print("AmountShift ({}) not possible "
                      "(house would be outside map)".format(amountShift))
                self.determineShift(currentHouse, directionShift)

        # recursive error catching
        # returning currenthouse from last valid determineShift attempt
        return currentHouse
