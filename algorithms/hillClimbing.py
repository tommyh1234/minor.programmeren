# -*- coding: UTF-8 -*-
import random
# from algorithms.randomalg import RandomAlgorithm
# from algorithms.speedrandom import SpeedRandomAlgorithm
from algorithms.greedy import GreedyAlgorithm



class HillClimbingAlgorithm(object):
    def __init__(self, area, fhAmount, bAmount, mAmount):
        self.isDone = False
        self.tryCount = 0
        self.initialGridPrice = 0
        self.area = area
        self.succesfullMoves = 0
        self.neutralMoves = 0
        self.unbeneficialMoves = 0
        self.totalHouseAmount = fhAmount + bAmount + mAmount
        self.pickHouseList = []
        # fill grid random
        self.randomAlg = GreedyAlgorithm(self.area,
                                         fhAmount,
                                         bAmount,
                                         mAmount)
        while(self.randomAlg.isDone is False):
            self.randomAlg.execute()

    def execute(self):

        # save initial value of grid
        if self.tryCount == 0:
            self.initialGridPrice = self.area.get_area_price()

        # total price grid
        currentTotalPrice = self.area.get_area_price()

        # pick random hous from list of placed houses,
        # making sure that all houses are visited once
        # before a house is revisited
        if self.tryCount % self.totalHouseAmount == 0:
            self.pickHouseList.extend(self.area.allHousesList)

        # keep track of amount of moves made
        self.tryCount += 1
        print("Move: {}".format(self.tryCount))

        currentHouse = random.choice(self.pickHouseList)

        # save coordinates of current house
        backupX = currentHouse.x
        backupY = currentHouse.y
        print('Original location house: ({}, {})'
              .format(currentHouse.x, currentHouse.y))

        # move house in a certain direction
        self.area.sliding_house(currentHouse, backupX, backupY)

        newTotalPrice = self.area.get_area_price()

        # compare old and new grid value, keep changes when higher
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
            print("✅ Price increase: {} | New grid value: {}"
                  .format(newTotalPrice
                          - currentTotalPrice,
                          currentTotalPrice))

        # remove last house from list of available options in next runs
        self.pickHouseList.remove(currentHouse)

        print("-------------------- ")

        if self.tryCount >= 2000:
            print("Total price: {} "
                  "Total price increase: {} "
                  "| In: ✅ {} succesfull | "
                  "😐 {} neutral | ❌ {} unbeneficial moves"
                  .format(currentTotalPrice,
                          currentTotalPrice - self.initialGridPrice,
                          self.succesfullMoves,
                          self.neutralMoves,
                          self.unbeneficialMoves))
            self.isDone = True
