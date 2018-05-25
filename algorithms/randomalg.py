# -*- coding: UTF-8 -*-
from algorithms.algorithm import Algorithm
from algorithms.constructionlist import construction_list
from algorithms.waterlist import water_list
import random


class RandomAlgorithm(Algorithm):

    def __init__(self, area, fhAmount, bAmount, mAmount,
                 placementOrder, waterAmountChoise, isEmpty=False):
        self.housesToPlace = construction_list(area,
                                               fhAmount,
                                               bAmount,
                                               mAmount)
        self.fhAmount = fhAmount
        self.bAmount = bAmount
        self.mAmount = mAmount
        self.waterAmount = 0
        self.watersToPlace = []
        self.waterPlacementRuns = 1
        self.housePlacementRuns = 1
        self.area = area
        self.placementOrder = placementOrder
        if waterAmountChoise <= 4:
            self.waterAmountChoise = waterAmountChoise
        else:
            self.waterAmountChoise = random.randint(1, 4)

    def execute(self):

        # determine amount of water to place and
        # make list with that many water objects
        if self.waterAmount == 0:
            self.waterAmount = self.waterAmountChoise
            self.watersToPlace = water_list(self.area, self.waterAmount)

        if len(self.housesToPlace) == 0:
            self.housesToPlace = construction_list(self.area,
                                                   self.fhAmount,
                                                   self.bAmount,
                                                   self.mAmount)

        # place water on map
        while len(self.watersToPlace) > 0:

            print('Run {} | Waters left: {}'.format(
                self.waterPlacementRuns, len(self.watersToPlace)))

            # choose first water from the list
            currentWater = random.choice(self.watersToPlace)

            # choose random x and y coordinates on the map
            xCor = random.randint(0, self.area.width - currentWater.width)
            yCor = random.randint(0, self.area.height - currentWater.height)
            print('Trying to place "{}" on ({}, {})'.format(currentWater,
                                                            xCor,
                                                            yCor))

            # only remove water from list if validly placed
            if not self.area.place_water(currentWater, xCor, yCor):
                print("✘ Cannot validly place water at"
                      " ({}, {})".format(xCor, yCor))
            else:
                self.watersToPlace.remove(currentWater)

            self.waterPlacementRuns += 1

        # place a house from the list on random coordinates
        if len(self.housesToPlace) > 0:
            print('Run {} | Houses left: {}'.format(
                self.housePlacementRuns, len(self.housesToPlace)))

            if self.placementOrder == 1:
                # choose random house from the list
                currentHouse = random.choice(self.housesToPlace)
            else:
                # choose first house from the list,
                # resulting in FH > Bung > Man
                currentHouse = self.housesToPlace[0]

            # choose random x and y coordinates on the map
            xCor = random.randint(currentHouse.minimumSpace,
                                  (self.area.width
                                   - currentHouse.width
                                   - currentHouse.minimumSpace))
            yCor = random.randint(currentHouse.minimumSpace,
                                  (self.area.height
                                   - currentHouse.height
                                   - currentHouse.minimumSpace))

            print('Trying to place "{}" on ({}, {})'.format(currentHouse,
                                                            xCor,
                                                            yCor))

            # only remove house from list if validly placed
            if not self.area.place_house(currentHouse, xCor, yCor):
                print("✘ Cannot validly place house at"
                      " ({}, {})".format(xCor, yCor))
            else:
                self.housesToPlace.remove(currentHouse)
            self.housePlacementRuns += 1

            # if a valid map can't be created in 1500 runs,
            # retry with a new random amount of water & and
            # the same amount of houses
            if self.housePlacementRuns >= 1500:
                print("❌ Could not make valid map in 1500 runs. Retrying...")

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

        if len(self.housesToPlace) == 0:
            print('✔ All houses placed ✔')

            # Recheck the validity of all houses (important to catch
            # invalid free space when houses with smaller free space
            # are placed after houses with larger free space)
            for house in self.area.allHousesList:
                if house.check_validity():
                    print("✔ {} validly placed".format(house))
                else:
                    print("✘ {} is not validly placed."
                          " Retrying...".format(house))
                    self.area.remove_house(house)
                    self.housesToPlace.append(house)

            self.area.get_area_price()
            if len(self.housesToPlace) == 0:
                print('Grid value: {}'.format(self.area.get_area_price()))
                self.isDone = True
