from objects.area import Area
from algorithms.randomalg import RandomAlgorithm


def main():

    amount = 0

    while amount != 20 or amount != 40 or amount != 60:
        amount = raw_input("20, 40 or 60 houses?: ")
            print("Amount houses not 20, 40 or 60")
   
    algorithm = RandomAlgorithm()

    grid0 = Area(amount)
    algorithm.fillRandomGrid(grid0, 36, 15, 9)

    grid1 = Area(amount)
    algorithm1 = RandomAlgorithm()
    algorithm1.fillRandomGrid(grid1, 36, 15, 9)


if __name__ == "__main__":
    main()
