from objects.area import Area
from visualizer import Visualizer
from algorithms.randomalg import RandomAlgorithm
from algorithms.speedrandom import SpeedRandomAlgorithm


def main():

    gridValues = []

    for i in range(0, 50):
        print("Run: {} | Start planning ...".format(i))
        grid = Area()
        algorithm = SpeedRandomAlgorithm()
        algorithm.execute(grid, 3, 5, 12)
        #visualizer = Visualizer(grid, algorithm)
        #visualizer.on_execute(9, 15, 36)
        gridValues.append(grid.get_area_price())
    print('###############################################################################')
    print('50 runs | Highest: {} | Lowest: {}'.format(max(gridValues), min(gridValues)))


if __name__ == "__main__":
    main()
