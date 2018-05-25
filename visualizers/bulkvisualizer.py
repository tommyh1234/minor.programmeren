from visualizers.visualizer import Visualizer
from datahelper import DataHelper
import copy


class BulkVisualizer(Visualizer):

    def __init__(self, area, algorithm, runs):
        super().__init__(area, algorithm)
        self.originalArea = copy.deepcopy(area)
        self.originalAlgorithm = copy.copy(algorithm)
        self.runs = 0
        self.allTimeHigh = 0
        self.dataHelper = DataHelper()
        self.maxRuns = runs

    def on_render(self):
        # run and render the algorithm
        super().on_render()
        # track the highest price
        if self.area.price > self.allTimeHigh:
            self.allTimeHigh = self.area.price

        # when a run is finished
        if self.algorithm.isDone is True and self.runs < self.maxRuns:
            print('Run {} is complete! 🎉'.format(self.runs))
            # Save the area after every run
            self.dataHelper.writeArea(self.area)

            # restore to a fresh state
            self.area = copy.deepcopy(self.originalArea)
            self.algorithm = copy.copy(self.originalAlgorithm)
            self.algorithm.area = self.area
            self.runs += 1

        if self.runs == self.maxRuns:
            print('I succesfully ran {} times!✨ '.format(self.runs))
