# -*- coding: UTF-8 -*-
import random
# from algorithms.randomalg import RandomAlgorithm
from algorithms.speedrandom import SpeedRandomAlgorithm


class HillClimbingAlgorithm(object):
    def __init__(self, area, fhAmount, bAmount, mAmount):
        self.isDone = False
        self.tryCount = 0
        self.area = area
        # fill grid random
        self.randomAlg = SpeedRandomAlgorithm(self.area, fhAmount, bAmount, mAmount)
        while(self.randomAlg.isDone is False):
            self.randomAlg.execute()

    def execute(self):

        # total price grid
        currentTotalPrice = self.area.get_area_price()

        # pick random houses from list of placed houses
        currentHouse = random.choice(self.area.allHousesList)

        # save coordinates of current house
        backupX = currentHouse.x
        backupY = currentHouse.y
        print('Original location house: ({}, {})'
              .format(currentHouse.x, currentHouse.y))

        # random choice wich type of move: switch,
        # turn, move house in direction
        # randomTypeOfMove = random.randint(0,2)

        # # move house in a certain direction
        # if randomTypeOfMove == 0
        self.area.sliding_house(currentHouse, backupX, backupY)

        # if the price from the grid didn't increased
        # go back to orignal location
        newTotalPrice = self.area.get_area_price()

        # if randomTypeOfMove == 0
        if currentTotalPrice > newTotalPrice:
            # remove moved house
            self.area.remove_house(currentHouse)

            # place house back at original location
            if not self.area.place_house(currentHouse,
                                         backupX,
                                         backupY):
                print("✘ Cannot validly place house at "
                      "({}, {})".format(currentHouse.x, currentHouse.y))
        
        self.tryCount += 1
        print("Move Nr.: {}".format(self.tryCount))

        if self.tryCount >= 100:
            self.isDone = True

        print("Grid value: {}".format(currentTotalPrice))
        print("-------------------- ")
