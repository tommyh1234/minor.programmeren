# -*- coding: UTF-8 -*-
import random
import math
from algorithms.randomalg import RandomAlgorithm
from algorithms.algorithm import Algorithm

# from algorithms.speedrandom import SpeedRandomAlgorithm


class HillClimbingAlgorithm(Algorithm):

    def __init__(self, area, fhAmount, bAmount, mAmount,
                 placementOrder=None, waterAmountChoice=None,
                 isEmpty=True, totalIterations=None,
                 beginTemp=None, endTemp=None,
                 typeOfSimulatedAnnealing=None,
                 correctionShortening=None):
        """Initiate all elements necessary for Hillclimbing or
            Simulated Annealing

            Keyword arguments:
            placementOrder                  --  determined the order of
                                                placement of the houses
            isDone                          --  checks all moves are done
            tryCount                        --  amount of current move
            succesfullMoves                 --  amount of succesfull moves
            succesfullSwitchCount           --  amount of succesfull switches
            succesfullTurnCount             --  amount of succesfull turns
            succesfullSlideCount            --  amount of succesfull slides
            neutralMoves                    --  amount of neutral moves
            neutralSlideCount               --  amount of neutral slides
            neutralTurnCount                --  amount of neutral turns
            neutralSwitchCount              --  amount of neutral switches
            unbeneficialMoves               --  amount of unbenficial moves
            unbeneficialSwitchCount         --  amount of unbenficial switches
            unbeneficialTurnCount           --  amount of unbenficial turn
            unbeneficialSlideCount          --  amount of unbenficial slides
            SAAcceptedUnbeneficialMoveCount --  amount of accepted unbenficial
                                                moves by Simulated Annealing
            SAAcceptedUnbeneficialSlideCount--  amount of accepted unbenficial
                                                slides by Simulated Annealing
            SAAcceptedUnbeneficialTurnCount --  amount of accepted unbenficial
                                                turns by Simulated Annealing
            SAAcceptedUnbeneficialSwitchCount-  amount of accepted unbenficial
                                                switches by Simulated Annealing
            SARejectedUnbeneficialMoveCount --  amount of rejected unbenficial
                                                moves by Simulated Annealing
            SARejectedUnbeneficialSlideCount--  amount of accepted unbenficial
                                                slides by Simulated Annealing
            SARejectedUnbeneficialTurnCount --  amount of accepted unbenficial
                                                turn by Simulated Annealing
            SARejectedUnbeneficialSwitchCount-- amount of accepted unbenficial
                                                switches by Simulated Annealing
            typeOfSimulatedAnnealing         -- the type of Simulated Annealing
            correctionShortening             -- the correction for the
                                                shortening, when you use
                                                Simulated Annealing
            initialGridPrice                --  orignal price off randomized
                                                grid
            area                            --  the area to place houses on
            beginTemp                       --  begin temperature of the
                                                Aimulated Annealing
            endTemp                         --  end temperature of the
                                                Aimulated Annealing
            totalIterations                 --  total iterations
            totalHouseAmount                --  total amount of houses
            pickHouseList                   --  list of houses
           """

        self.placementOrder = placementOrder
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
        self.SAAcceptedUnbeneficialMoveCount = 0
        self.SAAcceptedUnbeneficialSlideCount = 0
        self.SAAcceptedUnbeneficialTurnCount = 0
        self.SAAcceptedUnbeneficialSwitchCount = 0
        self.SARejectedUnbeneficialMoveCount = 0
        self.SARejectedUnbeneficialSlideCount = 0
        self.SARejectedUnbeneficialTurnCount = 0
        self.SARejectedUnbeneficialSwitchCount = 0
        self.typeOfSimulatedAnnealing = typeOfSimulatedAnnealing
        self.correctionShortening = correctionShortening
        self.initialGridPrice = 0
        self.area = area
        self.beginTemp = beginTemp
        self.endTemp = endTemp
        self.totalIterations = totalIterations
        self.totalHouseAmount = fhAmount + bAmount + mAmount
        self.pickHouseList = []

        if isEmpty is True:
            # fill grid random
            self.randomAlg = RandomAlgorithm(self.area,
                                             fhAmount,
                                             bAmount,
                                             mAmount,
                                             placementOrder,
                                             waterAmountChoice)
            while self.randomAlg.isDone is False:
                self.randomAlg.execute()

    def execute(self):
        """Runs one steop of the Hillclimber and the Simulated
        Annealing Algorithm"""

        # reset outcome of simulated annealing algorithm
        simulatedAnnealing = None

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
            # We don't do a simulated annealing when the grid is not decreased
            # in value. Because the acceptation chance is always bigger than 1.
            # So new grid will accept.
            if currentTotalPrice > newTotalPrice:
                # simulated annealing algorithm
                if self.beginTemp is not None:
                    # if simulated annealing accept new grid
                    simulatedAnnealing = self.simulated_annealing(
                                         self.typeOfSimulatedAnnealing,
                                         newTotalPrice,
                                         currentTotalPrice,
                                         self.beginTemp,
                                         self.endTemp,
                                         self.tryCount,
                                         self.totalIterations,
                                         self.correctionShortening)

                    # accept unbeneficial move by simulated annealing
                    if simulatedAnnealing is True:
                        self.SAAcceptedUnbeneficialSlideCount += 1
                        self.SAAcceptedUnbeneficialMoveCount += 1
                        print("⬇️ ✅  Unbeneficial move. Has been done by "
                              "Simulated Annealing.")
                        print("Price decrease: {} | New grid value: {}"
                              .format(newTotalPrice - currentTotalPrice,
                                      newTotalPrice))

                    # unbeneficial moves is rejected by simulated annealing
                    if simulatedAnnealing is False:
                        self.SARejectedUnbeneficialSlideCount += 1
                        self.SARejectedUnbeneficialMoveCount += 1
                        print("⬇️ ❌️  Unbeneficial move. Has been rejected by"
                              "Simulated Annealing.")

                # will not accept unbeneficial move
                if simulatedAnnealing is not True:
                    # remove current house
                    self.area.remove_house(currentHouse)

                    # place house back at origanal coordinates
                    if not self.area.place_house(currentHouse, backupX,
                                                 backupY):
                        print("✘ Cannot validly place house at "
                              "({}, {})".format(currentHouse.x,
                                                currentHouse.y))

                    if simulatedAnnealing is None:
                        self.unbeneficialMoves += 1
                        self.unbeneficialSlideCount += 1
                        print("❌ Unbeneficial move. Has been undone.")

            # neutral moves
            elif currentTotalPrice == newTotalPrice:
                self.neutralMoves += 1
                self.neutralSlideCount += 1
                print("😐 Neutral (allowed) or impossible move (reverted)")

            # beneficial moves
            else:
                self.succesfullSlideCount += 1
                self.succesfullMoves += 1
                print("✅ Price increase: {} | New grid value: {}"
                      .format(newTotalPrice
                              - currentTotalPrice,
                              currentTotalPrice))

        # turn a house 90degrees at its location
        if 6 <= randomTypeOfMove <= 8:

            print("TURN HOUSE")
            # check if the house is a not square (familyhome),
            kind = type(currentHouse).__name__
            while kind == "familyHome":
                # currentHouse = random.choice(self.pickHouseList)
                currentHouse = random.choice(self.area.allHousesList)

            # backup height and width of the house
            backupHeight = currentHouse.height
            backupWidth = currentHouse.width
            print('Original location house: ({}, {})'
                  .format(currentHouse.x, currentHouse.y))

            # turn house
            self.area.turn_house(currentHouse, backupWidth, backupHeight)

            # if the price from the grid didn't increased
            # go back to orignal location
            newTotalPrice = self.area.get_area_price()

            # accept move by a Hillclimber or simulated Annealing Algorithm
            # We don't do a simulated annealing when the grid is not decreased
            # in value. Because the acceptation chance is always bigger than 1.
            # So new grid will accept.
            if currentTotalPrice > newTotalPrice:
                # simulated annealing algorithm
                if self.beginTemp is not None:
                    # if simulated annealing accept new grid
                    simulatedAnnealing = self.simulated_annealing(
                                         self.typeOfSimulatedAnnealing,
                                         newTotalPrice,
                                         currentTotalPrice,
                                         self.beginTemp,
                                         self.endTemp,
                                         self.tryCount,
                                         self.totalIterations,
                                         self.correctionShortening)

                    # accept unbeneficial move by simulated annealing
                    if simulatedAnnealing is True:
                        self.SAAcceptedUnbeneficialTurnCount += 1
                        self.SAAcceptedUnbeneficialMoveCount += 1
                        print('⬇️ ✅  Unbeneficial move. Has been done by'
                              'Simulated Annealing.')
                        print("Price decrease: {} | New grid value: {}"
                              .format(newTotalPrice - currentTotalPrice,
                                      newTotalPrice))

                    # reject unbeneficial move by simulated annealing
                    if simulatedAnnealing is False:
                        self.SARejectedUnbeneficialTurnCount += 1
                        self.SARejectedUnbeneficialMoveCount += 1
                        print('⬇️ ❌️  Unbeneficial move. Has been rejected by,'
                              'Simulated Annealing.')

                # will not accept unbeneficial move
                if simulatedAnnealing is not True:
                    # turn house back to orignal height and length
                    if not self.area.turn_house(currentHouse,
                                                currentHouse.width,
                                                currentHouse.height):
                        print("✘ Cannot validly place house at "
                              "({}, {})".format(currentHouse.x,
                                                currentHouse.y))

                    if simulatedAnnealing is None:
                        self.unbeneficialMoves += 1
                        self.unbeneficialTurnCount += 1
                        print("❌ Unbeneficial move. Has been undone.")

            # count neutral value moves and turns
            elif currentTotalPrice == newTotalPrice:
                self.neutralMoves += 1
                self.neutralTurnCount += 1
                print("😐 Neutral (allowed) or impossible move (reverted)")

            # count amount of succefull moves and turns
            else:
                self.succesfullTurnCount += 1
                self.succesfullMoves += 1
                print("✅ Price increase: {} | New grid value: {}"
                      .format(newTotalPrice
                              - currentTotalPrice,
                              currentTotalPrice))

        # switch the position of two houses
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

            # Accept move by a Hillclimber or simulated Annealing Algorithm
            # We don't do a simulated annealing when the grid is not decreased
            # invalue. Because the acceptation chance is always bigger than 1.
            # So new grid will accept.
            if currentTotalPrice > newTotalPrice:

                # simulated annealing algorithm
                if self.beginTemp is not None:
                    # if simulated annealing accept new grid
                    simulatedAnnealing = self.simulated_annealing(
                                            self.typeOfSimulatedAnnealing,
                                            newTotalPrice,
                                            currentTotalPrice,
                                            self.beginTemp,
                                            self.endTemp,
                                            self.tryCount,
                                            self.totalIterations,
                                            self.correctionShortening)

                    # accept unbeneficial move by simulated annealing
                    if simulatedAnnealing is True:
                        self.SAAcceptedUnbeneficialSwitchCount += 1
                        self.SAAcceptedUnbeneficialMoveCount += 1
                        print('⬇️ ✅  Unbeneficial move. Has been done by'
                              'Simulated Annealing.')
                        print('Price decrease: {} | New grid value: {}'
                              .format(newTotalPrice - currentTotalPrice,
                                      currentTotalPrice))

                    # reject unbeneficial move by simulated annealing
                    if simulatedAnnealing is False:
                        self.SARejectedUnbeneficialSwitchCount += 1
                        self.SARejectedUnbeneficialMoveCount += 1
                        print('⬇️ ❌️  Unbeneficial move. Has been'
                              'rejected by Simulated Annealing.')

                # will not accept unbeneficial move
                if simulatedAnnealing is not True:
                    # remove houses from grid if not increased
                    self.area.remove_house(houseA)
                    self.area.remove_house(houseB)

                    # place orignal house A back on grid
                    if not self.area.place_house(houseA,
                                                 backupHouseAX,
                                                 backupHouseAY):
                        print("✘ Cannot validly place house at "
                              "({}, {})".format(currentHouse.x,
                                                currentHouse.y))

                    # place orignal house B back on grid
                    if not self.area.place_house(houseB,
                                                 backupHouseBX,
                                                 backupHouseBY):
                        print("✘ Cannot validly place house at "
                              "({}, {})".format(currentHouse.x,
                                                currentHouse.y))

                    # update counter for hillclimber
                    if simulatedAnnealing is None:
                        self.unbeneficialMoves += 1
                        self.unbeneficialSwitchCount += 1
                        print("❌ Unbeneficial move. Has been undone.")

            # Update counter of neutral moves
            elif currentTotalPrice == newTotalPrice:
                self.neutralMoves += 1
                self.neutralSlideCount += 1
                print("😐 Neutral (allowed) or impossible move (reverted)")

            # update counter of succefulmoves
            else:
                self.succesfullSlideCount += 1
                self.succesfullMoves += 1
                print("✅ Price increase: {} | New grid value: {}"
                      .format(newTotalPrice
                              - currentTotalPrice,
                              currentTotalPrice))

        # print total result of the hillclimber or simulated annealing
        print("-------------------- ")

        if self.tryCount >= self.totalIterations:
            print("Total price: {} "
                  "Total price increase: {} "
                  .format(currentTotalPrice,
                          currentTotalPrice - self.initialGridPrice))
            print("In: ✅ {} succesfull moves"
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
            print("In: ⬇️ ✅ {} Simulated Annealing accepted unbeneficial"
                  "({} slide(s), {} turn(s), {} switche(s)"
                  .format(self.SAAcceptedUnbeneficialMoveCount,
                          self.SAAcceptedUnbeneficialSlideCount,
                          self.SAAcceptedUnbeneficialTurnCount,
                          self.SAAcceptedUnbeneficialSwitchCount))
            print("In: ⬇️ ❌ {} Simulated Annealing rejected unbeneficial"
                  "({} slide(s), {} turn(s), {} switche(s)"
                  .format(self.SARejectedUnbeneficialMoveCount,
                          self.SARejectedUnbeneficialSlideCount,
                          self.SARejectedUnbeneficialTurnCount,
                          self.SARejectedUnbeneficialSwitchCount))

            self.isDone = True

    def simulated_annealing(self, typeOfSimulatedAnnealing,
                            newTotalPrice, currentTotalPrice,
                            beginTemp, endTemp,
                            tryCount, totalIterations,
                            correctionShortening):
        """ Algorithm that decide if a move will be accepted or rejected

            Keyword arguments:
            typeOfSimulatedAnnealing -- type of simulated annealing, lineair
                                        exponential, sigmoidal
            newTotalPrice            -- new price of the grid
            currentTotalPrice        -- original price of the grid
            beginTemp                -- begin temperature of the simulated
                                        annealing
            endTemp                  -- end temperature of the simulated
                                        annealing
            tryCount                 -- amount of moves
            totalIterations          -- total moves
            correctionShortening     -- correction for the shortening
        """

        currentTemp = 0
        endTemp += 0.000000000001

        # simulated annealing lineair
        if typeOfSimulatedAnnealing == 1:
            currentTemp = (beginTemp - tryCount * (beginTemp - endTemp) /
                           totalIterations)

        # simulated annealing exponential
        if typeOfSimulatedAnnealing == 2:
            currentTemp = (beginTemp * (endTemp/beginTemp) **
                           (tryCount / totalIterations))

        # simulated annealing sigmoidal
        if typeOfSimulatedAnnealing == 3:
            partOfCurrentTemp = (0.3 * (tryCount - totalIterations / 2))

            # if partofcurrentTemp is bigger than 50. reset as e^50 is to big.
            if partOfCurrentTemp > 50:
                partOfCurrentTemp = 50

            # calculate current temperature
            currentTemp = (endTemp + (beginTemp + endTemp) /
                           (1 + math.exp(partOfCurrentTemp)))

        # calculate shortening, coolinscheme and acception chance
        shortening = (newTotalPrice - currentTotalPrice) / correctionShortening
        coolingscheme = shortening / currentTemp
        if coolingscheme > 50:
            print('coolingscheme bigger than 50')
            coolingscheme = 50
        acceptationChance = math.exp(coolingscheme)
        print('After acceptationChance')
        randomValue = random.random()

        print('Grid Difference =', (newTotalPrice - currentTotalPrice),
              '| Shortening =', shortening, '| Current Temp. =', currentTemp,
              '| Coolingscheme =', coolingscheme)
        print('Acceptation Chance', acceptationChance,
              '| Random Value', randomValue)

        # move will be accepted if acceptation chance is bigger than random
        # value
        if acceptationChance > randomValue:
            return True

        else:
            return False
