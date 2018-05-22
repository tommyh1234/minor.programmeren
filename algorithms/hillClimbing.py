# -*- coding: UTF-8 -*-
import random
# from algorithms.randomalg import RandomAlgorithm
from algorithms.speedrandom import SpeedRandomAlgorithm


class HillClimbingAlgorithm(object):
    def __init__(self, area, fhAmount, bAmount, mAmount):
        self.isDone = False
        self.tryCount = 0
        self.initialGridPrice = 0
        self.area = area
        self.succesfullMoves = 0
        self.neutralMoves = 0
        self.unbeneficialMoves = 0
        # fill grid random
        self.randomAlg = SpeedRandomAlgorithm(self.area,
                                              fhAmount,
                                              bAmount,
                                              mAmount)
        while(self.randomAlg.isDone is False):
            self.randomAlg.execute()

    def execute(self):

        # save initial value of grid
        if self.tryCount == 0:
            self.initialGridPrice = self.area.get_area_price()

        # keep track of amount of moved made
        self.tryCount += 1
        print("Move: {}".format(self.tryCount))

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
            else:
                self.unbeneficialMoves += 1
                print("❌ Unbeneficial move. Has been undone.")
        elif currentTotalPrice == newTotalPrice:
            self.neutralMoves += 1
            print("😐 Neutral move. Allow to overcome local minima.")
        else:
            self.succesfullMoves += 1
            print("New grid value: {}".format(currentTotalPrice))
            print("✅ Price increase: {}".format(newTotalPrice
                                                - currentTotalPrice))
        print("-------------------- ")

        if self.tryCount >= 2000:
            print("Total price increase: {} "
                  "| In: ✅ {} succesfull | "
                  "😐 {} neutral | ❌ {} unbeneficial moves"
                  .format(currentTotalPrice - self.initialGridPrice,
                          self.succesfullMoves,
                          self.neutralMoves,
                          self.unbeneficialMoves))
            self.isDone = True
