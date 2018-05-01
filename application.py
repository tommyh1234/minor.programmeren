from objects.area import Area
from visualizer import Visualizer
from algorithms.randomalg import RandomAlgorithm


def main():
    amount = 0

    while (amount != 20 or amount != 40 or amount != 60):
        amount = input("20, 40 or 60 houses?: ")
        print("Amount houses not 20, 40 or 60")

    grid = Area()
    algorithm = RandomAlgorithm()
    visualizer = Visualizer(grid, algorithm)
    visualizer.on_execute(3, 15, 9)


if __name__ == "__main__":
    main()
