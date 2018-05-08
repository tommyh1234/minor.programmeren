from objects.area import Area
from algorithms.speedrandom import SpeedRandomAlgorithm
# from algorithms.hillClimbing import HillClimbingAlgorithm
# from algorithms.randomalg import RandomAlgorithm
from visualizer import Visualizer


def main():

    # looping the random algorithm 50 times ###
    # gridValues = []

    # for i in range(0, 50):
    #     print("Run: {} | Start planning ...".format(i))
    #     grid = Area()
    #     algorithm = SpeedRandomAlgorithm()
    #     algorithm.execute(grid, 12, 5, 3)
    #     gridValues.append(grid.get_area_price())
    # print('#########################################')
    # print('50 runs | Highest: {} | Lowest: {}'
    #       .format(max(gridValues), min(gridValues)))

    # just a hillclimber ###
    # grid = Area()
    # algorithm = HillClimbingAlgorithm(grid, 36, 15, 9)
    # visualizer = Visualizer(grid, algorithm)
    # visualizer.on_execute()

    grid = Area()
    algorithm = HillClimbingAlgorithm(grid, 36, 15, 9)
    visualizer = Visualizer(grid, algorithm)
    visualizer.on_execute()

if __name__ == "__main__":
    main()
