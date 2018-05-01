# -*- coding: UTF-8 -*-
from constructionlist import construction_list
import random


class RandomAlgorithm(object):

    def execute(self, area, fhAmount, bAmount, mAmount):
        houses = construction_list(area, fhAmount, bAmount, mAmount)

        # place a house from the list on random coordinates
        counter = 0
        while len(houses) > 0:
            print('Run {} | Houses left: {}'.format(counter, len(houses)))
            currentHouse = random.choice(houses)

            try:
                xCor = random.randint(0, area.width - currentHouse.width)
                yCor = random.randint(0, area.height - currentHouse.height)

                print('Trying to place "{}" on ({}, {})'.format(currentHouse,
                                                                xCor,
                                                                yCor))
                area.place_house(currentHouse, xCor, yCor)
                houses.remove(currentHouse)

            except RuntimeError:
                print("✘ Cannot validly place house at these coordinates.")
            counter += 1
        print('✓✓ All houses placed ✓✓')

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
                print("✓ {} validly placed".format(house))
            except RuntimeError:
                print("✘ {} is not validly placed.".format(house))

        print('Grid value: {}'.format(area.get_area_price()))
