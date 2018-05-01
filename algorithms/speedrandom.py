# -*- coding: UTF-8 -*-
from algorithms.constructionlist import construction_list
import random


class SpeedRandomAlgorithm(object):

    def execute(self, area, fhAmount, bAmount, mAmount):
        houses = construction_list(area, fhAmount, bAmount, mAmount)
        housesAmount = len(houses)

        # place a house from the list on random coordinates
        runCounter = 0
        failedPlacementCounter = 0
        checkValidPlacement = 0
        checkInvalidPlacement = 0

        while len(houses) > 0:
            runCounter += 1
            currentHouse = random.choice(houses)

            try:
                xCor = random.randint(0, area.width - currentHouse.width)
                yCor = random.randint(0, area.height - currentHouse.height)
                area.place_house(currentHouse, xCor, yCor)
                houses.remove(currentHouse)

            except RuntimeError:
                failedPlacementCounter += 1

        # create a list with all placed houses
        placedHouses = (area.familyHomeList
                        + area.bungalowList
                        + area.mansionList)

        # Recheck the validity of all houses (important to catch
        # invalid free space when houses with smaller free space
        # are placed after houses with larger free space)
        for house in placedHouses:
            try:
                house.check_validity()
                checkValidPlacement += 1
            except RuntimeError:
                checkInvalidPlacement += 1

        gridvalue = area.get_area_price()

        print('Placed {} houses | \
               Value: {} | \
               {} runs | \
               {} failed initial placements | \
               {} invalid placements on double check'
              .format(housesAmount,
                      gridvalue,
                      runCounter,
                      failedPlacementCounter,
                      checkInvalidPlacement))
