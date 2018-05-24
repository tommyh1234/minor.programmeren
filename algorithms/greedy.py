from algorithms.algorithm import Algorithm
from algorithms.constructionlist import construction_list
from algorithms.waterlist import water_list
import random


class GreedyAlgorithm(Algorithm):

    def __init__(self, area, fhAmount, bAmount, mAmount, isEmpty=True):
        self.housesToPlace = construction_list(area,
                                               fhAmount,
                                               bAmount,
                                               mAmount)
        self.waterAmount = 0
        self.watersToPlace = []
        self.area = area

    def execute(self):

        # determine amount of water to place and
        # make list with that many water objects
        if self.waterAmount == 0:
            self.waterAmount = random.randint(1, 4)
            self.watersToPlace = water_list(self.area, self.waterAmount)
