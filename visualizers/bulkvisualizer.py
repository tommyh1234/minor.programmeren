from visualizers.visualizer import Visualizer
from datahelper import DataHelper
import copy


class BulkVisualizer(Visualizer):
    """Draws consecutive visualisations for consecuetively created areas"""

    def __init__(self, area, algorithm, runs):
        """Initiate all elements necessary to run an algorithm consecutively
        and create consecutive visualizations for them.

        Keyword arguments:
        area      -- the area that should be visualised
        algorithm -- the algorithm by which the given area is filled
        runs      -- the amount of times the algorithm should be run and
                     the amount of visualizations to be made
        """

        super().__init__(area, algorithm)
        self.originalArea = copy.deepcopy(area)
        self.originalAlgorithm = copy.copy(algorithm)
        self.runs = 0
        self.allTimeHigh = 0
        self.dataHelper = DataHelper()
        self.maxRuns = runs

    def on_render(self):
        """Runs and visualizes the algorithm"""

        # visualize area
        super().on_render()

        # track highest found area value
        if self.area.price > self.allTimeHigh:
            self.allTimeHigh = self.area.price

        # when a run is finished...
        if self.algorithm.isDone is True and self.runs < self.maxRuns:

            # ...restore to a fresh state (empty area)
            self.area = copy.deepcopy(self.originalArea)
            self.algorithm = copy.copy(self.originalAlgorithm)
            self.algorithm.area = self.area

            # ...save values to csv file
            self.dataHelper.writeArea(self.area)
