from objects.area import Area
from visualizer import Visualizer
from algorithms.randomalg import RandomAlgorithm


def main():
    grid = Area()
    algorithm = RandomAlgorithm()
    visualizer = Visualizer(grid, algorithm)
    visualizer.on_execute(3, 15, 9)


if __name__ == "__main__":
    main()
