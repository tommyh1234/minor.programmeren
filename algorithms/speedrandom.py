# -*- coding: UTF-8 -*-
from algorithms.algorithm import Algorithm
from algorithms.constructionlist import construction_list
from algorithms.waterlist import water_list
import random


class SpeedRandomAlgorithm(Algorithm):


    def __init__(self, area, fhAmount, bAmount, mAmount, isEmpty=False):
        self.housesToPlace = construction_list(area,
                                               fhAmount,
                                               bAmount,
                                               mAmount)
        self.fhAmount = fhAmount
        self.bAmount = bAmount
        self.mAmount = mAmount
        self.waterAmount = 0
        self.watersToPlace = []
        self.totalIteration = totalIteration
        self.waterPlacementRuns = 1
        self.housePlacementRuns = 1
        self.area = area
        self.initPlacementFail = 0

    def execute(self):

        if self.housePlacementRuns == 1:
            print("Building random map. Please wait ...")

        # determine amount of water to place and
        # make list with that many water objects
        if self.waterAmount == 0:
            self.waterAmount = random.randint(1, 4)
            self.watersToPlace = water_list(self.area, self.waterAmount)

        # place water on map
        while len(self.watersToPlace) > 0:

            # choose first water from the list
            currentWater = random.choice(self.watersToPlace)

            # choose random x and y coordinates on the map
            xCor = random.randint(0, self.area.width - currentWater.width)
            yCor = random.randint(0, self.area.height - currentWater.height)

            # only remove water from list if validly placed
            if self.area.place_water(currentWater, xCor, yCor):
                self.watersToPlace.remove(currentWater)

            self.waterPlacementRuns += 1

        # place a house from the list on random coordinates
        if len(self.housesToPlace) > 0:

            # choose first house from the list, resulting in FH > Bung > Man
            currentHouse = self.housesToPlace[0]

            # choose random house from the list
            # currentHouse = random.choice(self.housesToPlace)

            # choose random x and y coordinates on the map
            xCor = random.randint(currentHouse.minimumSpace,
                                  (self.area.width
                                   - currentHouse.width
                                   - currentHouse.minimumSpace))
            yCor = random.randint(currentHouse.minimumSpace,
                                  (self.area.height
                                   - currentHouse.height
                                   - currentHouse.minimumSpace))

            # only remove house from list if validly placed
            if self.area.place_house(currentHouse, xCor, yCor):
                self.housesToPlace.remove(currentHouse)

            self.housePlacementRuns += 1
            print("Houses left to place: {}  "
                  .format(len(self.housesToPlace)), end="\r")

            # if a valid map can't be created in 1500 runs,
            # retry with a new random amount of water & and
            # the same amount of houses
            if self.housePlacementRuns >= 1500:
                print("✘ Could not make valid map in 1500 runs. Retrying...")

                # while-loop ensures all houses are removed
                while len(self.area.allHousesList) > 0:
                    for house in self.area.allHousesList:
                        self.area.remove_house(house)

                while len(self.area.allWatersList) > 0:
                    for water in self.area.allWatersList:
                        self.area.remove_water(water)

                self.waterAmount = 0
                self.watersToPlace = []
                self.waterPlacementRuns = 1
                self.housePlacementRuns = 1
                self.housesToPlace = []
                self.housesToPlace = construction_list(self.area,
                                                       self.fhAmount,
                                                       self.bAmount,
                                                       self.mAmount)

        else:
            # Recheck the validity of all houses (important to catch
            # invalid free space when houses with smaller free space
            # are placed after houses with larger free space)
            for house in self.area.allHousesList:
                if not house.check_validity():
                    self.initPlacementFail += 1
                    self.area.remove_house(house)
                    self.housesToPlace.append(house)

            if len(self.housesToPlace) == 0:
                print('Placed {} houses in {} runs and '
                      '{} water area(s) in {} runs | '
                      'Grid value: {} | '
                      '{} failed initial placements'
                      .format(len(self.area.allHousesList),
                              self.housePlacementRuns,
                              len(self.watersToPlace),
                              self.waterPlacementRuns,
                              self.area.get_area_price(),
                              self.initPlacementFail))
                print("-------------------- ")
                self.isDone = True
