# -*- coding: UTF-8 -*-
import random


class Area(object):
    """Create the area object in which the map will be saved"""
    width = 320
    height = 360

    def __init__(self):
        """Initiate all elements necessary to create an Area

        Keyword arguments:
        grid           -- the data structure all houses and waters are saved on
        allWatersList  -- list of all water objects placed on the grid
        allHousesList  -- list of all house objects placed on the grid
        mansionList    -- list of all mansion objects placed on the grid
        bungalowList   -- list of all bunalow objects placed on the grid
        familyHomeList -- list of all family home objects placed on the grid
        price          -- the current value of the configuration of the grid
        recursiveCount -- counter for the amount of recursion used in the
                          determineShift function
        """

        self.grid = [[None for y in range(self.height)]
                     for x in range(self.width)]
        self.allWatersList = []
        self.allHousesList = []
        self.mansionList = []
        self.bungalowList = []
        self.familyHomeList = []
        self.price = 0
        self.recursiveCount = None


    def surface(self):
        """Calculate the total surface of the area"""
        return self.width * self.height


    def place_water(self, water, xCoordinate, yCoordinate):
        """Place a water object on the grid

        Keyword arguments:
        water       -- the water object to be placed on the map
        xCoordinate -- the x-coordiante of that water object
        yCoordinate -- the y-xooridante of that water object
        """

        water.x = xCoordinate
        water.y = yCoordinate

        if water.check_validity():
            # place water object on every grid point
            # covered by the water
            for i in range(xCoordinate, xCoordinate + water.width):
                for j in range(yCoordinate, yCoordinate + water.height):
                    self.grid[i][j] = water

            # add water object to list of water objects
            self.allWatersList.append(water)
            return True

        return False


    def remove_water(self, water):
        """Remove a water object from the grid

        Keyword arguments:
        water -- the water object to be removed from the map
        """

        # remove water object from every grid point
        # covered by water
        for i in range(water.x, water.x + water.width):
            for j in range(water.y, water.y + water.height):
                self.grid[i][j] = None

        # remove water object to list of water objects
        self.allWatersList.remove(water)


    def place_house(self, house, xCoordinate, yCoordinate):
        """Place a house object on the grid

        Keyword arguments:
        house       -- the house object to be placed on the map
        xCoordinate -- the x-coordinate of that house object
        yCoordinate -- the y-xooridante of that house object
        """

        house.x = xCoordinate
        house.y = yCoordinate
        kind = type(house).__name__

        if house.check_validity():
            # place house object on every grid point
            # covered by house
            for i in range(xCoordinate, xCoordinate + house.width):
                for j in range(yCoordinate, yCoordinate + house.height):
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

        return False


    def remove_house(self, house):
        """Remove a house object from the grid

        Keyword arguments:
        house -- the house object to be removed from the map
        """

        # remove house object from every grid point
        # covered by house
        for i in range(house.x, house.x + house.width):
            for j in range(house.y, house.y + house.height):
                self.grid[i][j] = None
        kind = type(house).__name__

        # remove house object from approporiate list
        self.allHousesList.remove(house)
        if kind == "Mansion":
            self.mansionList.remove(house)
        elif kind == "Bungalow":
            self.bungalowList.remove(house)
        elif kind == "FamilyHome":
            self.familyHomeList.remove(house)


    def check_house_balance(self):
        """Check ratio of placed houses for required ratio's"""

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
        """Check the grid price house by house"""

        totalPrice = 0
        counter = 0

        # check value of all houses and their freespace
        # invalid house is worth 0
        while counter < len(self.allHousesList):
            if self.allHousesList[counter].check_validity() is False:
                return 0

            totalPrice += self.allHousesList[counter].get_price()
            counter += 1

        self.price = totalPrice
        return totalPrice


    def sliding_house(self, currentHouse, backupX, backupY):
        """Slide a house up/down or left/right by a certain amount

        Keyword arguments:
        currentHouse -- the house object to be slided
        backupX      -- the original x-coordinate of that house
        backupY      -- the original y-cooridante of that house
        """

        # remove original house from map
        self.remove_house(currentHouse)

        # determine distance to move and update house coordinates
        directionShift = None
        houseIsBlocked = None
        currentHouse = self.determine_shift(currentHouse, directionShift,
                                           houseIsBlocked)

        # if house cannot be placed at new coordinates,
        # put it back at orignial coordinates
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


    def determine_shift(self, currentHouse, directionShift, houseIsBlocked):
        """Determine the direction and amount to shift a house with

        Keyword arguments:
        currentHouse   -- the house object that the shift
                          should be determined for
        directionShift -- the amount of half meters the house
                          will be shifted with
        houseIsBlocked -- whether a house is surrounded by other house,
                          which makes a shift impossible
        """

        # first time a shift is determined for the same house,
        # reset recursive count and house is blocked counter
        if houseIsBlocked is None:
            houseIsBlocked = 0
            self.recursiveCount = 0

        # if house is surrounded by other houses and
        # thus cannot move, return currentHouse with invalid
        # coordinates and thus skip the shifiting of this house
        if houseIsBlocked > 1:
            print("SWIFTHOUSE FUNCTION NOT POSSIBLE - House is locked in")
            # return last (invalid) currentHouse
            return currentHouse

        # choose to move house horizontally or verticallly
        if directionShift is None:
            directionShift = random.randint(0, 1)
            print("Direction: {}".format(directionShift))

        # pick random distance between -5 and 5 (not 0) to shift house with
        options = list(range(-5, 5+1))
        options.remove(0)
        amountShift = random.choice(options)
        print("amountShift: {}".format(amountShift))

        # move house in chosen direction,
        # but only if it still falls within the map
        if directionShift == 0:
            tempCurrentHouseX = currentHouse.x + amountShift
            tempBoundry = (self.width
                           - currentHouse.width
                           - currentHouse.minimumSpace)
            # check if coordinates of shifted house would be inside map
            if (tempCurrentHouseX > currentHouse.minimumSpace and
                    tempCurrentHouseX < tempBoundry):
                currentHouse.x += amountShift
                return currentHouse
            else:
                print("❌ amountShift ({}) not possible "
                      "(house would be outside map)".format(amountShift))
                self.recursiveCount += 1
                print("RecursiveCount (dir 0):", self.recursiveCount)

                # change direction from horizontal to vertical
                # if a horizontal shift wasn't possible in 50 tries
                if self.recursiveCount >= 50:
                    directionShift = 1
                    houseIsBlocked += 1
                    print(houseIsBlocked)
                    self.determine_shift(currentHouse, directionShift,
                                         houseIsBlocked)
                else:
                    self.determine_shift(currentHouse, directionShift,
                                         houseIsBlocked)

        else:
            tempCurrentHouseY = currentHouse.y + amountShift
            tempBoundry = (self.height
                           - currentHouse.height
                           - currentHouse.minimumSpace)
            # check if coordinates of shifted house would be inside map
            if (tempCurrentHouseY > currentHouse.minimumSpace and
                    tempCurrentHouseY < tempBoundry):
                currentHouse.y += amountShift
                return currentHouse
            else:
                print("❌ AmountShift ({}) not possible "
                      "(house would be outside map)".format(amountShift))
                self.recursiveCount += 1
                print("RecursiveCount (dir 1):", self.recursiveCount)

                # change direction from vertical to horizontal
                # if a vertical shift wasn't possible in 50 tries
                if self.recursiveCount >= 50:
                    directionShift = 0
                    houseIsBlocked += 1
                    print(houseIsBlocked)
                    self.determine_shift(currentHouse, directionShift,
                                         houseIsBlocked)
                else:
                    self.determine_shift(currentHouse, directionShift,
                                         houseIsBlocked)

        # recursive error catching
        # return currenthouse from last valid determine_shift attempt
        return currentHouse


    def turn_house(self, currentHouse, backupWidth, backupHeight):
        """Turn a house on its side (switching its width and height)

        Keyword arguments:
        currentHouse -- the house object that should be turned
        backupWidth  -- the original width of that house
        backupHeight -- the original width of that house
        """

        # remove house from map
        self.remove_house(currentHouse)

        # turn house width and height
        currentHouse.width = backupHeight
        currentHouse.height = backupWidth

        # check if the turned house can be validly placed within the grid
        turnValidity = self.check_house_is_inside_grid(currentHouse)

        # if house will not be inside map after turning,
        # put it back in original orientation
        if turnValidity is False:
            currentHouse.width = backupWidth
            currentHouse.height = backupHeight

        # if another house is in the way of the turned house,
        # put it back in original orientation
        if self.place_house(currentHouse,
                            currentHouse.x,
                            currentHouse.y) is False:
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
        """Switch positions of two houses

        Keyword arguments:
        houseA -- first of the house objects that should be switched
        houseB -- other house objects that should be switched
        """

        # check if switched houses coud validly be
        # placed within grid after switching
        checkValidityBoundarySwitchA = self.check_house_is_inside_grid(houseA)
        checkValidityBoundarySwitchB = self.check_house_is_inside_grid(houseB)
        if ((checkValidityBoundarySwitchA is True and
             checkValidityBoundarySwitchB is True)):

            # backup houses' coordination
            backUpHouseAX = houseA.x
            backUpHouseAY = houseA.y
            backUpHouseBX = houseB.x
            backUpHouseBY = houseB.y

            # remove houses from grid
            self.remove_house(houseA)
            self.remove_house(houseB)

            # switch both houses' coordinates
            houseA.x = backUpHouseBX
            houseA.y = backUpHouseBY
            houseB.x = backUpHouseAX
            houseB.y = backUpHouseAY

            # place houses on new locations
            aSucces = self.place_house(houseA, houseA.x, houseA.y)
            bSucces = self.place_house(houseB, houseB.x, houseB.y)

            # check if houses are placed succesful,
            # if not remove two houses
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
        """Check if a house falls within the grid

        Keyword arguments:
        house -- the house objects that should be checked
        """

        if house.x > (self.width - house.width - house.minimumSpace):
            return False
        if house.y > (self.height - house.height - house.minimumSpace):
            return False
        
        return True
