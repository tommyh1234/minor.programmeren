from objects.area import Area
from visualizer import Visualizer
from algorithms.randomalg import RandomAlgorithm


def main():
    grid = Area()
    algorithm = RandomAlgorithm(grid, 9, 15, 36)
    visualizer = Visualizer(grid, algorithm)
    visualizer.on_execute()


if __name__ == "__main__":
    main()
