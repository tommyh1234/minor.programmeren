# -*- coding: UTF-8 -*-
import random
from algorithms.randomalg import RandomAlgorithm
from algorithms.algorithm import Algorithm
from algorithms.simulatedannealing import simulatedAnnealing
# from algorithms.speedrandom import SpeedRandomAlgorithm

class HillClimbingAlgorithm(Algorithm):
    def __init__(self,\
                 area,\
                 fhAmount,\
                 bAmount,\
                 mAmount,\
                 isEmpty=True,\
                 beginTemp = None,\
                 endTemp = None,\
                 totalIteration = None,\
                 currentIteration = None):
       
        self.isDone = False
        self.tryCount = 0
        self.succesfullMoves = 0
        self.succesfullSwitchCount = 0
        self.succesfullTurnCount = 0
        self.succesfullSlideCount = 0
        self.neutralMoves = 0
        self.neutralSlideCount = 0
        self.neutralTurnCount = 0
        self.neutralSwitchCount = 0
        self.unbeneficialMoves = 0
        self.unbeneficialSwitchCount = 0
        self.unbeneficialTurnCount = 0
        self.unbeneficialSlideCount = 0
        self.initialGridPrice = 0
        self.area = area
        self.totalHouseAmount = fhAmount + bAmount + mAmount
        self.pickHouseList = []

        if isEmpty is True:
            # fill grid random
            self.randomAlg = RandomAlgorithm(self.area,
                                             fhAmount,
                                             bAmount,
                                             mAmount)
            while self.randomAlg.isDone is False:
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
        print("Move: {} | ".format(self.tryCount), end='')

        # currentHouse = random.choice(self.pickHouseList)
        currentHouse = random.choice(self.area.allHousesList)

        # save coordinates of current house
        backupX = currentHouse.x
        backupY = currentHouse.y

        # random choice wich type of move: switch,
        # turn, move house in direction
        randomTypeOfMove = random.randint(0, 11)

        # move house in a certain direction
        if 0 <= randomTypeOfMove <= 5:
            print("SLIDING HOUSE")
            print('Original location house: ({}, {})'
                  .format(currentHouse.x, currentHouse.y))
            self.area.sliding_house(currentHouse, backupX, backupY)

            # if the price from the grid didn't increased
            # go back to orignal location
            newTotalPrice = self.area.get_area_price()

            # accept move by a Hillclimber or simulated Annealing Algorithm
            # We don't do a simulated annealing when the grid is not decreased in
            # value. Because the acceptation change is always bigger than 1. So
            # new grid will accept. 
            if currentTotalPrice > newTotalPrice:
                
                # hillclimbing algorithm
                if hillClimbingOrSimulatedAnnealing == 1:

                    # remove current house
                    self.area.remove_house(currentHouse)

                    # place house back at origanal coordinates
                    if not self.area.place_house(currentHouse, backupX, backupY):
                      print("✘ Cannot validly place house at "
                            "({}, {})".format(currentHouse.x, currentHouse.y))

                    self.unbeneficialMoves += 1
                    self.unbeneficialSlideCount += 1
                    print("❌ Unbeneficial move. Has been undone.")

                # simulated annealing algorithm
                elif hillClimbingOrSimulatedAnnealing == 2:
                    
                    if self.simulatedannealing.simulatedAnnealing(currentPrice,\
                                                               originalPrice,\
                                                               endTemp,\
                                                               typeOfSimulatedAnnealing,\
                                                               totalIteration,\
                                                               currentIteration)\
                                                               == False:
                        # remove current house
                        self.area.remove_house(currentHouse)

                        # place house back at origanal coordinates
                        if not self.area.place_house(currentHouse, backupX, backupY):
                          print("✘ Cannot validly place house at "
                                "({}, {})".format(currentHouse.x, currentHouse.y))

                        self.unbeneficialMoves += 1
                        self.unbeneficialSlideCount += 1
                        print("❌ Unbeneficial move. Has been undone.")

            elif currentTotalPrice == newTotalPrice:
                self.neutralMoves += 1
                self.neutralSlideCount += 1
                print("😐 Neutral (allowed) or impossible move (reverted)")
            
            else:
                self.succesfullSlideCount += 1
                self.succesfullMoves += 1
                print("✅ Price increase: {} | New grid value: {}"
                      .format(newTotalPrice
                              - currentTotalPrice,
                              currentTotalPrice))

        # turn house on the same location
        if 6 <= randomTypeOfMove <= 8:

            print("TURN HOUSE")
            # check if the house is a not square (familyhome),
            # turning no value
            kind = type(currentHouse).__name__
            while kind == "familyHome":
                # currentHouse = random.choice(self.pickHouseList)
                currentHouse = random.choice(self.area.allHousesList)

            backupHeight = currentHouse.height
            backupWidth = currentHouse.width
            print('Original location house: ({}, {})'
                  .format(currentHouse.x, currentHouse.y))

            # turn house
            self.area.turn_house(currentHouse, backupWidth, backupHeight)

            # if the price from the grid didn't increased
            # go back to orignal location
            newTotalPrice = self.area.get_area_price()

            # accept move by a Hillclimber or simulated Annealing Algorithm.
            # We don't do a simulated annealing when the grid is not decreased in
            # value. Because the acceptation change is always bigger than 1. So
            # new grid will accept. 
            if currentTotalPrice > newTotalPrice:
              
                # hillclimbing algorithm
                if hillClimbingOrSimulatedAnnealing == 1:

                    # turn house back to orignal height and length
                    if not self.area.turn_house(currentHouse, currentHouse.width,
                                                currentHouse.height):
                        print("✘ Cannot validly place house at "
                              "({}, {})".format(currentHouse.x, currentHouse.y))

                    self.unbeneficialMoves += 1
                    self.unbeneficialTurnCount += 1
                    print("❌ Unbeneficial move. Has been undone.")

                # simulated annealing algorithm
                if hillClimbingOrSimulatedAnnealing == 2:
                    
                    if self.simulatedannealing.simulatedAnnealing(currentPrice,\
                                                               originalPrice,\
                                                               endTemp,\
                                                               typeOfSimulatedAnnealing,\
                                                               totalIteration,\
                                                               currentIteration)\
                                                               == False:

                        # turn house back to orignal height and length
                        if not self.area.turn_house(currentHouse, currentHouse.width,
                                                    currentHouse.height):
                            print("✘ Cannot validly place house at "
                                  "({}, {})".format(currentHouse.x, currentHouse.y))

                    self.unbeneficialMoves += 1
                    self.unbeneficialTurnCount += 1
                    print("❌ Unbeneficial move. Has been undone.")

            elif currentTotalPrice == newTotalPrice:
                self.neutralMoves += 1
                self.neutralTurnCount += 1
                print("😐 Neutral (allowed) or impossible move (reverted)")
            else:
                self.succesfullTurnCount += 1
                self.succesfullMoves += 1
                print("✅ Price increase: {} | New grid value: {}"
                      .format(newTotalPrice
                              - currentTotalPrice,
                              currentTotalPrice))

        # switch two houses
        if 9 <= randomTypeOfMove <= 11:

            print("SWITCH HOUSE")
            houseA = currentHouse

            # pick random houses from list of houses
            houseB = random.choice(self.area.allHousesList)

            # make shure you pick two different houses
            while type(houseA).__name__ == type(houseB).__name__:
                houseB = random.choice(self.area.allHousesList)
                print("Chose house of same type to switch with, "
                      "picking new house")

            # backup coordinates of houses
            backupHouseAX = houseA.x
            backupHouseAY = houseA.y
            backupHouseBX = houseB.x
            backupHouseBY = houseB.y
            print('Original locations: houseA: ({}, {}) | houseB: ({}, {})'
                  .format(houseA.x, houseA.y, houseB.x, houseB.y))

            # switch houses
            self.area.switch_house(houseA, houseB)

            # get price of grid
            newTotalPrice = self.area.get_area_price()

            # accept move by a Hillclimber or simulated Annealing Algorithm
            # We don't do a simulated annealing when the grid is not decreased in
            # value. Because the acceptation change is always bigger than 1. So
            # new grid will accept. 
            if currentTotalPrice > newTotalPrice:
              
                if hillClimbingOrSimulatedAnnealing == 1:
                    # remove houses from grid if not increased
                    self.area.remove_house(houseA)
                    self.area.remove_house(houseB)

                    # place orignal houses back on grid
                    if not self.area.place_house(houseA,
                                               backupHouseAX,
                                               backupHouseAY):
                      print("✘ Cannot validly place house at "
                            "({}, {})".format(currentHouse.x,
                                              currentHouse.y))

                    if not self.area.place_house(houseB,
                                               backupHouseBX,
                                               backupHouseBY):
                      print("✘ Cannot validly place house at "
                            "({}, {})".format(currentHouse.x,
                                              currentHouse.y))

                    self.unbeneficialMoves += 1
                    self.unbeneficialSwitchCount += 1
                    print("❌ Unbeneficial move. Has been undone.")


                # simulated annealing algorithm
                if hillClimbingOrSimulatedAnnealing == 2:
                    # TODO HILLCLIMBING ALGORITHM
                    pass

            elif currentTotalPrice == newTotalPrice:
              self.neutralMoves += 1
              self.neutralSwitchCount += 1
              print("😐 Neutral (allowed) or impossible move (reverted)")
            else:
              self.succesfullSwitchCount += 1
              self.succesfullMoves += 1
              print("✅ Price increase: {} | New grid value: {}"
                    .format(newTotalPrice
                            - currentTotalPrice,
                            currentTotalPrice))

    def simulated_annealing(self, currentPrice,\
                            originalPrice,\
                            endTemp,\
                            typeOfSimulatedAnnealing,\
                            totalIteration,\
                            currentIteration):

        self.currentPrice = currenTemp
        self.originalPrice = originalPrice
        self.beginTemp = beginTemp
        self.endTemp = endTemp
        self.typeOfSimulatedAnnealing = typeOfSimulatedAnnealing        
        self.totalIteration = totalIteration
        self.currentIteration = currentIteration

        # Lineair 
        if typeOfSimulatedAnnealing == 1:
                self.currenTemp = (beginTemp - currentIteration * 
                                  (beginTemp - endTemp) / totalIteration)

        # Exponential
        if typeOfSimulatedAnnealing == 2:
                self.currenTemp = (beginTemp * (endTemp/beginTemp) ^ 
                                   (currentIteration / totalIteration))

        # Sigmoidal
        if typeOfSimulatedAnnealing == 3:
                self.currenTemp = (endTemp + (beginTemp + endTemp) / 
                (1 + exp(0.3 (currentIteration - totalIteration / 2)))) 

        shortening = (currentPrice - originalPrice) / originalPrice
        coolingscheme = shortening / currenTemp
        acceptationChange = exp(coolingscheme)

        currentIteration += 1

        if acceptationChange < random.random():
            return False



        # # remove last house from list of available options in next runs
        # self.pickHouseList.remove(currentHouse)

        print("-------------------- ")


        if self.tryCount >= totalIteration:
            print("Total price: {} "
                  "Total price increase: {} "
                  .format(currentTotalPrice,
                          currentTotalPrice - self.initialGridPrice))
            print("In: ✅ {} succesfull moves "
                  "({} slide(s), {} turn(s), {} switche(s)"
                  .format(self.succesfullMoves,
                          self.succesfullSlideCount,
                          self.succesfullTurnCount,
                          self.succesfullSwitchCount))
            print("    😐 {} neutral or impossible moves "
                  "({} slide(s), {} turn(s), {} switche(s))"
                  .format(self.neutralMoves,
                          self.neutralSlideCount,
                          self.neutralTurnCount,
                          self.neutralSwitchCount))
            print("    ❌ {} unbeneficial moves "
                  "({} slide(s), {} turn(s), {} switche(s))"
                  .format(self.unbeneficialMoves,
                          self.unbeneficialSlideCount,
                          self.unbeneficialTurnCount,
                          self.unbeneficialSwitchCount))

            self.isDone = True
