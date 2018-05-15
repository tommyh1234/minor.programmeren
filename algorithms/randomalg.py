# -*- coding: UTF-8 -*-
from algorithms.algorithm import Algorithm
from algorithms.constructionlist import construction_list
import random


class RandomAlgorithm(Algorithm):

    def __init__(self, area, fhAmount, bAmount, mAmount):
        self.houses = construction_list(area, fhAmount, bAmount, mAmount)
        self.counter = 0
        self.area = area

    def execute(self):

        # place a house from the list on random coordinates
        if len(self.houses) > 0:
            print('Run {} | Houses left: {}'.format(
                self.counter, len(self.houses))
                 )

            # choose first house from the list, resulting in FH > Bung > Man
            currentHouse = self.houses[0]

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
                print("Cannot validly place house at"
                      " ({}, {})".format(xCor, yCor))
            else:
                self.houses.remove(currentHouse)

            self.counter += 1
        else:
            print('✓✓ All houses placed ✓✓')
            self.isDone = True

            # create a list with all placed houses
            placedHouses = []
            placedHouses.extend(self.area.familyHomeList)
            placedHouses.extend(self.area.bungalowList)
            placedHouses.extend(self.area.mansionList)

            # Recheck the validity of all houses (important to catch
            # invalid free space when houses with smaller free space
            # are placed after houses with larger free space)
            for house in placedHouses:
                try:
                    house.check_validity()
                    print("✓ {} validly placed".format(house))
                except RuntimeError:
                    print("✘ {} is not validly placed.".format(house))

            print('Grid value: {}'.format(self.area.get_area_price()))
