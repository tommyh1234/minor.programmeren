# -*- coding: UTF-8 -*-
import random


class Area(object):
    width = 320
    height = 360

    def __init__(self):
        self.grid = [[None for y in range(self.height)]
                     for x in range(self.width)]
        self.mansionList = []
        self.bungalowList = []
        self.familyHomeList = []
        self.allHousesList = []

    def place_house(self, house, x, y):
        house.x = x
        house.y = y
        kind = type(house).__name__

        # place new house
        if house.check_validity():
            # place the house on every coordinate
            # that is covered by the house
            try:
                for i in range(x, x + house.width):
                    for j in range(y, y + house.height):
                        self.grid[i][j] = house
                # add the house to the appropriate lists
                self.allHousesList.append(house)
                if kind == "Mansion":
                    self.mansionList.append(house)
                elif kind == "Bungalow":
                    self.bungalowList.append(house)
                elif kind == "FamilyHome":
                    self.familyHomeList.append(house)
                return True

            # TODO TRY EXCEPT DOESN'T WORK
            except IndexError:
                # catch case where a swapt house would be out if map
                print("switch out of range")
                return False
        else:
            print("✘ Cannot validly place house at "
                  "({}, {})".format(house.x, house.y))
            return False

    def remove_house(self, house):
        for i in range(house.x, house.x + house.width):
            for j in range(house.y, house.y + house.height):
                self.grid[i][j] = None
        kind = type(house).__name__
        self.allHousesList.remove(house)
        if kind == "Mansion":
            self.mansionList.remove(house)
        elif kind == "Bungalow":
            self.bungalowList.remove(house)
        elif kind == "FamilyHome":
            self.familyHomeList.remove(house)

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
        # checking grid price house by house, invalid maps get value of 0

        totalPrice = 0
        counter = 0

        while counter < len(self.allHousesList):
            if self.allHousesList[counter].check_validity() is False:
                return 0

            totalPrice += self.allHousesList[counter].get_price()
            counter += 1

        return totalPrice

    def sliding_house(self, currentHouse, backupX, backupY):
        # remove house from map
        self.remove_house(currentHouse)

        # determine distance to move and update house coordinates
        directionShift = None
        currentHouse = self.determineShift(currentHouse, directionShift)

        # if house cannot be placed at new coordinates, put it back
        if self.place_house(currentHouse,
                            currentHouse.x,
                            currentHouse.y) is False:

            if self.place_house(currentHouse, backupX, backupY):
                print("✓ Put house back at "
                      "original location ({}, {})"
                      .format(backupX, backupY))
            else:
                print("Could not put house back "
                      "at original location ({}, {})"
                      .format(backupX, backupY))
        else:
            print("✓ House placed at new location ({}, {})"
                  .format(currentHouse.x, currentHouse.y))

    def determineShift(self, currentHouse, directionShift):

        # choose to move horizontal or vertical
        if directionShift is None:
            directionShift = random.randint(0, 1)
            print("Direction: {}".format(directionShift))

        # pick random distance to shift the house with
        amountShift = random.randint(-30, 30)
        print("amountShift: {}".format(amountShift))

        # move house in chosen direction,
        # but only if it still falls within the map
        recursiveCount = 0
        if directionShift == 0:
            tempCurrentHouseX = currentHouse.x + amountShift
            tempBoundry = (self.width
                           - currentHouse.width
                           - currentHouse.minimumSpace)
            if (tempCurrentHouseX > currentHouse.minimumSpace and
                    tempCurrentHouseX < tempBoundry):
                currentHouse.x += amountShift
                return currentHouse
            else:
                print("amountShift ({}) not possible "
                      "(house would be outside map)".format(amountShift))
                recursiveCount += 1

                # change directoin from horizontal to vertical after 50 tries
                if recursiveCount > 50:
                    directionShift = 1
                    self.determineShift(currentHouse, directionShift)
                else:
                    self.determineShift(currentHouse, directionShift)

        else:
            tempCurrentHouseY = currentHouse.y + amountShift
            tempBoundry = (self.height
                           - currentHouse.height
                           - currentHouse.minimumSpace)
            if (tempCurrentHouseY > currentHouse.minimumSpace and
                    tempCurrentHouseY < tempBoundry):
                currentHouse.y += amountShift
                return currentHouse
            else:
                print("AmountShift ({}) not possible "
                      "(house would be outside map)".format(amountShift))
                recursiveCount += 1

                # change directoin from vertical to horizontal after 50 tries
                if recursiveCount > 50:
                    directionShift = 0
                    self.determineShift(currentHouse, directionShift)
                else:
                    self.determineShift(currentHouse, directionShift)

        # recursive error catching
        # returning currenthouse from last valid determineShift attempt
        return currentHouse

    def turn_house(self, currentHouse, backupWidth, backupHeight):

        # remove house from map
        self.remove_house(currentHouse)

        # turn house width and height
        currentHouse.width = backupHeight
        currentHouse.height = backupWidth

        # if house cannot be placed at new coordinates, put it back
        if self.place_house(currentHouse,
                            currentHouse.x,
                            currentHouse.y) is False:

            # place house back with orignal width and height
            currentHouse.width = backupWidth
            currentHouse.height = backupHeight

            if self.place_house(currentHouse, currentHouse.x, currentHouse.y):
                print("✓ Put house back at "
                      "original location ({}, {})"
                      .format(currentHouse.x, currentHouse.y))
            else:
                print("Could not put house back "
                      "at original location ({}, {})"
                      .format(currentHouse.x, currentHouse.y))
        else:
            print("✓ House placed at new location ({}, {})"
                  .format(currentHouse.x, currentHouse.y))

    def switch_house(self, houseA, houseB):
        # backup coordination of houses
        backUpHouseAX = houseA.x
        backUpHouseAY = houseA.y

        backUpHouseBX = houseB.x
        backUpHouseBY = houseB.y

        # remove houses from grid
        self.remove_house(houseA)
        self.remove_house(houseB)

        # switch coordinates of the houses
        houseA.x = backUpHouseBX
        houseA.y = backUpHouseBY
        houseB.x = backUpHouseAX
        houseB.y = backUpHouseAY

        # place house at new location
        aSucces = self.place_house(houseA, houseA.x, houseA.y)
        bSucces = self.place_house(houseB, houseB.x, houseB.y)

        print("before")
        print(aSucces)
        print(bSucces)
        # check if houses are placed succesful, if not remove two houses
        if any([aSucces is False, bSucces is False]):

            print("after")
            print(aSucces)
            print(bSucces)

            if bSucces is False:
                self.remove_house(houseA)
                print("removed A")

            if aSucces is False:
                self.remove_house(houseB)
                print("removed B")

            # give houses oringnal location back
            houseA.x = backUpHouseAX
            houseA.y = backUpHouseAY
            houseB.x = backUpHouseBX
            houseB.y = backUpHouseBY

            # place house back at orignal location
            self.place_house(houseA, houseA.x, houseA.y)
            self.place_house(houseB, houseB.x, houseB.y)
