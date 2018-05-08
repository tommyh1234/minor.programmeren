# -*- coding: UTF-8 -*-
from algorithms.constructionlist import construction_list
import random


class SpeedRandomAlgorithm(object):

    def __init__(self, area, fhAmount, bAmount, mAmount):
        self.houses = construction_list(area, fhAmount, bAmount, mAmount)
        self.housesAmount = len(self.houses)
        self.counter = 0
        self.area = area
        self.runCounter = 0
        self.failedPlacementCounter = 0
        self.checkValidPlacement = 0
        self.checkInvalidPlacement = 0

    def execute(self):

        # place a house from the list on random coordinates
        while len(self.houses) > 0:
            self.runCounter += 1
            currentHouse = random.choice(self.houses)

            try:
                xCor = random.randint(0, (self.area.width
                                          - currentHouse.width))
                yCor = random.randint(0, (self.area.height
                                          - currentHouse.height))
                self.area.place_house(currentHouse, xCor, yCor)
                self.houses.remove(currentHouse)

            except RuntimeError:
                self.failedPlacementCounter += 1

        # create a list with all placed houses
        placedHouses = (self.area.familyHomeList
                        + self.area.bungalowList
                        + self.area.mansionList)

        # Recheck the validity of all houses (important to catch
        # invalid free space when houses with smaller free space
        # are placed after houses with larger free space)
        for house in placedHouses:
            try:
                house.check_validity()
                self.checkValidPlacement += 1
            except RuntimeError:
                self.checkInvalidPlacement += 1

        gridvalue = self.area.get_area_price()

        print('Placed {} houses | \
               Value: {} | \
               {} runs | \
               {} failed initial placements | \
               {} invalid placements on double check'
              .format(self.housesAmount,
                      gridvalue,
                      self.runCounter,
                      self.failedPlacementCounter,
                      self.checkInvalidPlacement))
