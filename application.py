from objects.area import Area
# from algorithms.speedrandom import SpeedRandomAlgorithm
from algorithms.hillClimbing import HillClimbingAlgorithm
# from algorithms.greedy import GreedyAlgorithm
# from algorithms.randomalg import RandomAlgorithm
from visualizer import Visualizer
#from bulkvisualizer import BulkVisualizer


def main():

    # # just Random algorithm
    # grid = Area()
    # algorithm = RandomAlgorithm(grid, 36, 15, 9)  # 20h: 12, 5, 3
    # #                                             # 40: 24, 10, 6
    # #                                             # 60: 36, 15, 9
    # visualizer = Visualizer(grid, algorithm)
    # visualizer.on_execute()

    # # just greedy algorithm
    # grid = Area()
    # algorithm = GreedyAlgorithm(grid, 36, 15, 9)  # 20h: 12, 5, 3
    # #                                             # 40: 24, 10, 6
    # #                                             # 60: 36, 15, 9
    # visualizer = Visualizer(grid, algorithm)
    # visualizer.on_execute()

    # # just SpeedRandom Algorithm
    # grid = Area()
    # algorithm = SpeedRandomAlgorithm(grid, 36, 15, 9)  # 20h: 12, 5, 3
    # #                                                  # 40: 24, 10, 6
    # #                                                  # 60: 36, 15, 9
    # visualizer = BulkVisualizer(grid, algorithm, 10)
    # visualizer.on_execute()

    # just a HillClimbing algorithm
    grid = Area()
    algorithm = HillClimbingAlgorithm(grid, 36, 15, 9)  # 20h: 12, 5, 3
    #                                                   # 40: 24, 10, 6
    #                                                   # 60: 36, 15, 9
    visualizer = Visualizer(grid, algorithm)
    visualizer.on_execute()


if __name__ == "__main__":
    main()
