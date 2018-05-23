# -*- coding: UTF-8 -*-
import random
from algorithms.speedrandom import SpeedRandomAlgorithm
# from algorithms.speedrandom import SpeedRandomAlgorithm


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
        # self.pickHouseList = []
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

        # total price grid
        currentTotalPrice = self.area.get_area_price()

        # pick random house from list of placed houses,
        # making sure that all houses are visited once
        # before a house is revisited
        # if self.tryCount % self.totalHouseAmount == 0:
        #     self.pickHouseList.extend(self.area.allHousesList)

        # keep track of amount of moves made
        self.tryCount += 1
        print("Move: {}".format(self.tryCount))

        # currentHouse = random.choice(self.pickHouseList)
        currentHouse = random.choice(self.area.allHousesList)

        # save coordinates of current house
        backupX = currentHouse.x
        backupY = currentHouse.y
        print('Original location house: ({}, {})'
              .format(currentHouse.x, currentHouse.y))

        # random choice wich type of move: switch,
        # turn, move house in direction
        randomTypeOfMove = random.randint(0, 2)


        # move house in a certain direction
        if randomTypeOfMove == 0:
            print("Move: SLIDING HOUSE")
            self.area.sliding_house(currentHouse, backupX, backupY)

            # if the price from the grid didn't increased
            # go back to orignal location
            newTotalPrice = self.area.get_area_price()

            # check if grid is increased
            if currentTotalPrice > newTotalPrice:

                # remove current house
                self.area.remove_house(currentHouse)

                # place house back at origanal coordinates
                if not self.area.place_house(currentHouse, backupX, backupY):
                    print("✘ Cannot validly place house at "
                          "({}, {})".format(currentHouse.x, currentHouse.y))

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

        # turn house on the same location
        if randomTypeOfMove == 1:

            print("Move: TURN HOUSE")
            # check if the house is a not square (familyhome),
            # turning no value
            kind = type(currentHouse).__name__
            while kind == "familyHome":
                # currentHouse = random.choice(self.pickHouseList)
                currentHouse = random.choice(self.area.allHousesList)

            backupHeight = currentHouse.height
            backupWidth = currentHouse.width

            # turn house
            self.area.turn_house(currentHouse, backupWidth, backupHeight)

            # if the price from the grid didn't increased
            # go back to orignal location
            newTotalPrice = self.area.get_area_price()

            # check if grid is increased
            if currentTotalPrice > newTotalPrice:

                # turn house back to orignal height and length
                if not self.area.turn_house(currentHouse, currentHouse.width,
                                            currentHouse.height):
                    print("✘ Cannot validly place house at "
                          "({}, {})".format(currentHouse.x, currentHouse.y))

                self.unbeneficialMoves += 1
                print("❌ Unbeneficial move. Has been undone.")


            elif currentTotalPrice == newTotalPrice:
                self.neutralMoves += 1
                print("😐 Back to orignal location or equal move")
            else:
                self.succesfullMoves += 1
                print("✅ Price increase: {} | New grid value: {}"
                      .format(newTotalPrice
                              - currentTotalPrice,
                              currentTotalPrice))

        # switch two houses
        if randomTypeOfMove == 2:

            print("Move: SWITCH HOUSE")
            houseA = currentHouse

            # pick random houses from list of houses
            houseB = random.choice(self.area.allHousesList)

            # make shure you pick two different houses
            while type(houseA).__name__ == type(houseB).__name__:
                houseB = random.choice(self.area.allHousesList)
                print("the same type house, so pick random new house")

            # backup coordinates of houses
            backupHouseAX = houseA.x
            backupHouseAY = houseA.y
            backupHouseBX = houseB.x
            backupHouseBY = houseB.y

            # switch houses
            self.area.switch_house(houseA, houseB)

            # get price of grid
            newTotalPrice = self.area.get_area_price()

            # check if price grid is increased
            if currentTotalPrice > newTotalPrice:
                # remove houses from grid if not increased
                self.area.remove_house(houseA)
                self.area.remove_house(houseB)

                # place orignal houses back on grid
                if not self.area.place_house(houseA,
                                      backupHouseAX,
                                      backupHouseAY):
                        print("✘ Cannot validly place house at "
                                  "({}, {})".format(currentHouse.x, currentHouse.y))

                if not self.area.place_house(houseB,
                                      backupHouseBX,
                                      backupHouseBY):
                        print("✘ Cannot validly place house at "
                        "({}, {})".format(currentHouse.x, currentHouse.y))

                self.unbeneficialMoves += 1
                print("❌ Unbeneficial move. Has been undone.")
            elif currentTotalPrice == newTotalPrice:
                self.neutralMoves += 1
                print("😐 Back to orignal location or equal move.")
            else:
                self.succesfullMoves += 1
                print("✅ Price increase: {} | New grid value: {}"
                      .format(newTotalPrice
                              - currentTotalPrice,
                              currentTotalPrice))

        # # remove last house from list of available options in next runs
        # self.pickHouseList.remove(currentHouse)

        print("-------------------- ")

        if self.tryCount >= 1000:
            print("Total price increase: {} "
                  "| In: ✅ {} succesfull | "
                  "😐 {} neutral | ❌ {} unbeneficial moves"
                  .format(currentTotalPrice,
                          currentTotalPrice - self.initialGridPrice,
                          self.succesfullMoves,
                          self.neutralMoves,
                          self.unbeneficialMoves))

            self.isDone = True
