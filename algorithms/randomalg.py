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
            currentHouse = random.choice(self.houses)

            try:
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
                self.area.place_house(currentHouse, xCor, yCor)
                self.houses.remove(currentHouse)

            except RuntimeError:
                print("✘ Cannot validly place house at these coordinates.")
            self.counter += 1
        else:
            print('✓✓ All houses placed ✓✓')
            self.isDone = True

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
                    print("✓ {} validly placed".format(house))
                except RuntimeError:
                    print("✘ {} is not validly placed.".format(house))

            print('Grid value: {}'.format(self.area.get_area_price()))
