from objects.area import Area
# from algorithms.speedrandom import SpeedRandomAlgorithm
from algorithms.hillClimbing import HillClimbingAlgorithm
# from algorithms.randomalg import RandomAlgorithm
from bulkvisualizer import BulkVisualizer

from datahelper import DataHelper


def main():

    # just Random algorithm
    grid = Area()
    algorithm = HillClimbingAlgorithm(grid, 36, 15, 9, True)  # 20h: 12, 5, 3
    #                                                         # 40: 24, 10, 6
    #                                                         # 60: 36, 15, 9
    visualizer = BulkVisualizer(grid, algorithm, 1)
    visualizer.on_execute()

    # # just SpeedRandom Algorithm
    # grid = Area()
    # algorithm = SpeedRandomAlgorithm(grid, 36, 15, 9)  # 20h: 12, 5, 3
    # #                                                  # 40: 24, 10, 6
    # #                                                  # 60: 36, 15, 9
    # visualizer = BulkVisualizer(grid, algorithm, 10)
    # visualizer.on_execute()

    # # just a HillClimbing algorithm
    # grid = Area()
    # algorithm = HillClimbingAlgorithm(grid, 36, 15, 9)  # 20h: 12, 5, 3
    # #                                                   # 40: 24, 10, 6
    # #                                                   # 60: 36, 15, 9
    # visualizer = BulkVisualizer(grid, algorithm, 10)
    # visualizer.on_execute()


if __name__ == "__main__":
    main()
