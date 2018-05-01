from objects.area import Area
from algorithms.randomalg import RandomAlgorithm


def main():
    algorithm = RandomAlgorithm()

    grid0 = Area()
    algorithm.fillRandomGrid(grid0, 36, 15, 9)

    grid1 = Area()
    algorithm1 = RandomAlgorithm()
    algorithm1.fillRandomGrid(grid1, 36, 15, 9)


if __name__ == "__main__":
    main()
