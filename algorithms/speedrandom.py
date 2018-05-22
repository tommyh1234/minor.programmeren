# -*- coding: UTF-8 -*-
from algorithms.algorithm import Algorithm
from algorithms.constructionlist import construction_list
import random


class SpeedRandomAlgorithm(Algorithm):

    def __init__(self, area, fhAmount, bAmount, mAmount):
        self.housesToPlace = construction_list(area,
                                               fhAmount,
                                               bAmount,
                                               mAmount)
        self.counter = 0
        self.area = area
        self.initPlacementFail = 0

    def execute(self):

        if self.counter == 0:
            print("Building random map. Please wait ...")

        # place a house from the list on random coordinates
        if len(self.housesToPlace) > 0:

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

            # only remove house from list if validly placed
            if self.area.place_house(currentHouse, xCor, yCor):
                self.housesToPlace.remove(currentHouse)

            self.counter += 1
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
                print('Placed {} houses in {} runs | '
                      'Grid value: {} | '
                      '{} failed initial placements'
                      .format(len(self.area.allHousesList),
                              self.counter,
                              self.area.get_area_price(),
                              self.initPlacementFail))
                print("-------------------- ")
                self.isDone = True
