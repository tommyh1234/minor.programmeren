from algorithms.algorithm import Algorithm
from algorithms.constructionlist import construction_list
from objects.water import Water
import math


class GreedyAlgorithm(Algorithm):

    def __init__(self, area, fhAmount, bAmount, mAmount, isEmpty=True):
        self.housesToPlace = construction_list(area,
                                               fhAmount,
                                               bAmount,
                                               mAmount)
        self.housePlacementRuns = 0
        self.waterAmount = 0
        self.watersToPlace = []
        self.area = area
        self.currentX = 0
        self.currentY = 0
        self.maxFreeSpace = 12
        self.previousHouse = None

    def execute(self):

        # add 1 water area in de lower right corner
        if self.housePlacementRuns == 0:
            water = Water(self.area)
            dimension = math.ceil(math.sqrt(self.area.surface() * 0.2))
            water.width = dimension
            water.height = dimension
            self.area.place_water(water,
                                  self.area.width - dimension,
                                  self.area.height - dimension)

        # place a house from the list next to previous house
        if len(self.housesToPlace) > 0:
            print('Run {} | Houses left: {}'.format(
                self.housePlacementRuns, len(self.housesToPlace)))

            # choose first house from the list, resulting in Man > Bung > FH
            currentHouse = self.housesToPlace[0]

            # choose x and y coordinates on the map
            if self.previousHouse:
                xCor = self.currentX + self.previousHouse.minimumSpace
                yCor = self.currentY + 12
            else:
                xCor = self.currentX + currentHouse.minimumSpace
                yCor = self.currentY + 12

            # update x with width of house
            self.currentX = self.currentX + currentHouse.width + 12

            # if outside of map on right side, swith to row below
            if xCor >= (self.area.width
                        - currentHouse.width
                        - currentHouse.minimumSpace):
                print("hier")
                self.currentX = currentHouse.minimumSpace
                self.currentY = (self.currentY
                                 + self.previousHouse.minimumSpace
                                 + self.previousHouse.height
                                 + self.previousHouse.minimumSpace
                                 + 24)
                xCor = self.currentX
                yCor = self.currentY + 12
                self.currentX -= currentHouse.minimumSpace

                # update x with width of house
                self.currentX = (self.currentX
                                 + currentHouse.width
                                 + currentHouse.minimumSpace)

            print('Trying to place "{}" on ({}, {})'.format(currentHouse,
                                                            xCor,
                                                            yCor))

            # only remove house from list if validly placed
            if not self.area.place_house(currentHouse, xCor, yCor):
                print("✘ Cannot validly place house at"
                      " ({}, {})".format(xCor, yCor))
            else:
                self.housesToPlace.remove(currentHouse)
                self.previousHouse = currentHouse

            self.housePlacementRuns += 1

        else:
            print('✔ All houses placed ✔')

            # Recheck the validity of all houses (important to catch
            # invalid free space when houses with smaller free space
            # are placed after houses with larger free space)
            for house in self.area.allHousesList:
                if house.check_validity():
                    print("✔ {} validly placed".format(house))
                else:
                    print("✘ {} is not validly placed."
                          " Retrying...".format(house))
                    self.area.remove_house(house)
                    self.housesToPlace.append(house)

                self.isDone = True

            print('Grid value: {}'.format(self.area.get_area_price()))
