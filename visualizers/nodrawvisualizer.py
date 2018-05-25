from datahelper import DataHelper


class NoDrawVisualizer:
    """Runs an algorithm without visualization"""

    def __init__(self, area, algorithm):
        """Initiate all elements necessary to run an algorithm
        without visualization

        Keyword arguments:
        area      -- the area that should be used in the algoritm
        algorithm -- the algorithm by which the given area is filled
        """

        self.area = area
        self.algorithm = algorithm
        self.dataHelper = DataHelper()

    def on_execute(self):
        """Starts and executes the algorithm"""

        # while algorithm is not done, run it
        while self.algorithm.isDone is False:
            self.algorithm.execute()

            # save area state between every step
            self.dataHelper.writeArea(self.area)
