import random 
from algorithms.randomalg import RandomAlgorithm
from objects.area import Area

class HillClimbingAlgorithm(object):

    def excute(self, area, fhAmount, bAmount, mAmount):

        # fill grid random
        currentGrid = RandomAlgorithm()
        currentGrid.fillRandomGrid(area, fhAmount, bAmount, mAmount)

        currentTotalPrice = area.get_area_price()

        # make list of all houses
        houseList = []
        houseList.extend(area.mansionList)
        houseList.extend(area.familyHomeList)
        houseList.extend(area.bungalowList)
        
        print('houselist: {}'.format(houseList))

        # pick random houses
        currentHouse = random.choice(houseList)

        print('currentHouse: {}'.format(currentHouse))

        ## save x and y house
        backupX = currentHouse.x
        backupY = currentHouse.y

        print('currentHouseX: {}'.format(currentHouse.x))
        print('currentHouseY: {}'.format(currentHouse.y))

        # random move
        AmountShift = random.randint( -10, 10)
        print(AmountShift)

        # move to horizontal or vertical 
        DirectionShift = random.randint(0, 1)
        print(DirectionShift)

        # remove house
        area.remove_house(currentHouse)

        # change house in direction
        if DirectionShift == 0:
            self.currentHouse.x += AmountShift
        else:
            self.currentHouse.y += AmountShift

        # place new house
        try:
            area.place_house(currentHouse)
        except RuntimeError:
            print ("not valid location for house")

        # check if value of grid is increased
        newTotalPrice = area.get_area_price()

        if currentTotalPrice > newTotalPrice:

            # remove new house
            area.remove_house(currentHouse)

            # remove house and place origanal house
            currentHouse.x = backupX
            currentHouse.y = backupY

            # place new house
            are.place_house(currentHouse)
 