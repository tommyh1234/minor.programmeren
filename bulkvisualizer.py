from visualizer import Visualizer
import copy
from datahelper import DataHelper


class BulkVisualizer(Visualizer):

    def __init__(self, area, algorithm, runs):
        super().__init__(area, algorithm)
        self.originalArea = copy.deepcopy(area)
        self.originalAlgorithm = copy.copy(algorithm)
        self.runs = 0
        self.allTimeHigh = 0
        self.dataHelper = DataHelper()

    def on_render(self):
        super().on_render()
        if self.area.price > self.allTimeHigh:
            self.allTimeHigh = self.area.price

        if self.algorithm.isDone is True:
            self.area = copy.deepcopy(self.originalArea)
            self.algorithm = copy.copy(self.originalAlgorithm)
            self.algorithm.area = self.area
            self.scores = []
            self.lastPrice = 0
            self.dataHelper.writeArea(self.area)
