# -*- coding: UTF-8 -*-
from algorithms.algorithm import Algorithm
from algorithms.constructionlist import construction_list
from algorithms.waterlist import water_list
import random


class RandomAlgorithm(Algorithm):

    def __init__(self, area, fhAmount, bAmount, mAmount):
        self.housesToPlace = construction_list(area,
                                               fhAmount,
                                               bAmount,
                                               mAmount)
        self.waterAmount = 0
        self.watersToPlace = []
        self.waterPlacementRuns = 1
        self.housePlacementRuns = 1
        self.area = area

    def execute(self):

        # determine amount of water to place and
        # make list with that many water objects
        if self.waterAmount == 0:
            self.waterAmount = random.randint(1, 4)
            self.watersToPlace = water_list(self.area, self.waterAmount)

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

            # choose first house from the list, resulting in Man > Bung > FH
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

            # if no valid map in 1500 runs, exit the program
            if self.housePlacementRuns >= 1500:
                self.isDone = True
                raise RuntimeError("1500 Runs, can't create valid map")

        else:
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

            if len(self.housesToPlace) == 0:
                self.isDone = True

            print('Grid value: {}'.format(self.area.get_area_price()))
