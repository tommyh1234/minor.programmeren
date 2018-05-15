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
        else:
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
            print("✘ Cannot validly place house at"
                  " ({}, {})".format(currentHouse.x, currentHouse.y))
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
