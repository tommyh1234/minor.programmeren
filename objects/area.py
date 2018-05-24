# -*- coding: UTF-8 -*-
import random


class Area(object):
    width = 320
    height = 360

    def __init__(self):
        self.grid = [[None for y in range(self.height)]
                     for x in range(self.width)]
        self.waterList = []
        self.mansionList = []
        self.bungalowList = []
        self.familyHomeList = []
        self.allHousesList = []
        self.price = 0
        self.recursiveCount = 0

    def surface(self):
        return self.width * self.height

    def place_water(self, water, x, y):
        water.x = x
        water.y = y

        # place new piece of water
        if water.check_validity():
            # place the water on every coordinate
            # that is covered by the water
            for i in range(x, x + water.width):
                for j in range(y, y + water.height):
                    self.grid[i][j] = water
            # add the water to the list of water instances
            self.waterList.append(water)
            return True
        else:
            return False

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

        self.price = totalPrice
        return totalPrice

    def sliding_house(self, currentHouse, backupX, backupY):
        # remove house from map
        self.remove_house(currentHouse)

        # determine distance to move and update house coordinates
        directionShift = None
        houseIsBlocked = 0
        currentHouse = self.determineShift(currentHouse, directionShift,
                                           houseIsBlocked)

        # if house cannot be placed at new coordinates, put it back
        if self.place_house(currentHouse,
                            currentHouse.x,
                            currentHouse.y) is False:
            print("✘ Cannot validly place house at "
                  "({}, {})".format(currentHouse.x, currentHouse.y))
            if self.place_house(currentHouse, backupX, backupY):
                print("✔ Put house back at "
                      "original location ({}, {})"
                      .format(backupX, backupY))
            else:
                print("✘ Could not put house back "
                      "at original location ({}, {})"
                      .format(backupX, backupY))
        else:
            print("✔ House placed at new location ({}, {})"
                  .format(currentHouse.x, currentHouse.y))

    def determineShift(self, currentHouse, directionShift, houseIsBlocked):

        # choose to move horizontal or vertical
        if directionShift is None:
            directionShift = random.randint(0, 1)
            print("Direction: {}".format(directionShift))

        # pick random distance to shift the house with
        amountShift = random.randint(-5, 5)
        print("amountShift: {}".format(amountShift))

        # move house in chosen direction,
        # but only if it still falls within the map
        self.recursiveCount = 0

        # if house is surrounded by other houses and
        # thus cannot move
        if houseIsBlocked > 1:
            print("SWIFTHOUSE FUNCTION NOT POSSIBLE - House is locked in")
            # return last (invalid) currentHouse
            return currentHouse

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
                print("❌ amountShift ({}) not possible "
                      "(house would be outside map)".format(amountShift))
                self.recursiveCount += 1

                # change directoin from horizontal to vertical after 50 tries
                if self.recursiveCount > 50:
                    print("Recursion! (dir 0")
                    directionShift = 1
                    houseIsBlocked += 1
                    print(houseIsBlocked)
                    self.determineShift(currentHouse, directionShift,
                                        houseIsBlocked)
                else:
                    self.determineShift(currentHouse, directionShift,
                                        houseIsBlocked)

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
                print("❌ AmountShift ({}) not possible "
                      "(house would be outside map)".format(amountShift))
                self.recursiveCount += 1

                # change directoin from vertical to horizontal after 50 tries
                if self.recursiveCount > 50:
                    print("Recursion! dir 1")
                    directionShift = 0
                    houseIsBlocked += 1
                    print(houseIsBlocked)
                    self.determineShift(currentHouse, directionShift,
                                        houseIsBlocked)
                else:
                    self.determineShift(currentHouse, directionShift,
                                        houseIsBlocked)

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
                      "original location ({}, {}) Height: {}  Width: {}"
                      .format(currentHouse.x,
                              currentHouse.y,
                              currentHouse.height,
                              currentHouse.width))
            else:
                print("Could not put house back "
                      "at original location ({}, {})"
                      .format(currentHouse.x, currentHouse.y))
        else:
            print("✓ House placed at new location ({}, {})"
                  .format(currentHouse.x, currentHouse.y))

    def switch_house(self, houseA, houseB):

        # check if house coud valid placed on grid
        checkValidityBoundarySwitchA = self.check_house_is_inside_grid(houseA)
        checkValidityBoundarySwitchB = self.check_house_is_inside_grid(houseB)

        if ((checkValidityBoundarySwitchA is True and
             checkValidityBoundarySwitchB is True)):

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

            aSucces = self.place_house(houseA, houseA.x, houseA.y)
            bSucces = self.place_house(houseB, houseB.x, houseB.y)

            # check if houses are placed succesful, if not remove two houses
            if any([(aSucces is False and bSucces is True),
                    (bSucces is False and aSucces is True)]):
                if bSucces is False:
                    self.remove_house(houseA)

                if aSucces is False:
                    self.remove_house(houseB)

                # place house back at orignal location
                self.place_house(houseA, backUpHouseAX, backUpHouseAY)
                self.place_house(houseB, backUpHouseBX, backUpHouseBY)

            if any([aSucces is False and bSucces is False]):
                # place house back at orignal location
                self.place_house(houseA, backUpHouseAX, backUpHouseAY)
                self.place_house(houseB, backUpHouseBX, backUpHouseBY)

    def check_house_is_inside_grid(self, house):

        # check if house is entirely inside the grid
        if house.x > (self.width - house.width - house.minimumSpace):
            return False
        if house.y > (self.height - house.height - house.minimumSpace):
            return False
        else:
            return True
