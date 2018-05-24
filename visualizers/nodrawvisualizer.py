from datahelper import DataHelper


class NoDrawVisualizer:
    def __init__(self, area, algorithm):
        self.area = area
        self.algorithm = algorithm
        self.dataHelper = DataHelper()

    def on_execute(self):
        while self.algorithm.isDone is False:
            self.algorithm.execute()
            # save the state between every step
            self.dataHelper.writeArea(self.area)
