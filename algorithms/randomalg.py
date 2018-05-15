# -*- coding: UTF-8 -*-
from algorithms.algorithm import Algorithm
from algorithms.constructionlist import construction_list
import random


class RandomAlgorithm(Algorithm):

    def __init__(self, area, fhAmount, bAmount, mAmount):
        self.housesToPlace = construction_list(area,
                                               fhAmount,
                                               bAmount,
                                               mAmount)
        self.counter = 0
        self.area = area

    def execute(self):

        # place a house from the list on random coordinates
        if len(self.housesToPlace) > 0:
            print('Run {} | Houses left: {}'.format(
                self.counter, len(self.housesToPlace))
                 )

            # choose first house from the list, resulting in FH > Bung > Man
            currentHouse = random.choice(self.housesToPlace)

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

            self.counter += 1
        else:
            print('✓✓ All houses placed ✓✓')

            # Recheck the validity of all houses (important to catch
            # invalid free space when houses with smaller free space
            # are placed after houses with larger free space)
            for house in self.area.allHousesList:
                if house.check_validity():
                    print("✓ {} validly placed".format(house))
                else:
                    print("✘ {} is not validly placed."
                          " Retrying...".format(house))
                    self.area.remove_house(house)
                    self.housesToPlace.append(house)

            if len(self.housesToPlace) == 0:
                self.isDone = True

            print('Grid value: {}'.format(self.area.get_area_price()))
