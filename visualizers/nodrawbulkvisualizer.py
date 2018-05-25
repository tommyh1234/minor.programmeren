import copy
from datahelper import DataHelper


class NoDrawBulkVisualizer:
    """Runs an algorithm several times without visualization"""

    def __init__(self, area, algorithm, runs):
        """Initiate all elements necessary to run an algorithm consecutively
        without visualizations.

        Keyword arguments:
        area      -- the area that should be visualised
        algorithm -- the algorithm by which the given area is filled
        runs      -- the amount of times the algorithm should run
        """
        self.area = area
        self.algorithm = algorithm
        self.originalArea = copy.deepcopy(area)
        self.originalAlgorithm = copy.copy(algorithm)
        self.runs = 0
        self.dataHelper = DataHelper()
        self.maxRuns = runs

    def on_execute(self):
        """Executes an algorithm several times"""

        while self.runs < self.maxRuns:
            # continue running until algorithm is done
            while self.algorithm.isDone is False:
                self.algorithm.execute()

            # if algorithm completes one run, reset state
            if self.algorithm.isDone is True and self.runs < self.maxRuns:
                print('Run {} is complete! 🎉'.format(self.runs))
                # save area to csv
                self.dataHelper.writeArea(self.area)

                # reset area and algorithm
                self.area = copy.deepcopy(self.originalArea)
                self.algorithm = copy.copy(self.originalAlgorithm)
                self.algorithm.area = self.area
                self.runs += 1

            if self.runs == self.maxRuns:
                print('✨✨ I succesfully ran {}'
                      'times! ✨✨'.format(self.runs))
