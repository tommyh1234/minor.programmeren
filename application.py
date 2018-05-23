from objects.area import Area

from algorithms.speedrandom import SpeedRandomAlgorithm
from algorithms.hillClimbing import HillClimbingAlgorithm
from algorithms.randomalg import RandomAlgorithm

from visualizer import Visualizer
from bulkvisualizer import BulkVisualizer

from datahelper import DataHelper


def main():
    print("WELCOME TO AMSTELHAEGE")
    gridChoice = int(input('Do you want to load in a grid or start from scratch?\
                            1: Load a grid\
                            2: Start from scratch'))
    algorithmChoice = int(input('What algorithm do you want to run?\
                                1: Random \
                                2: SpeedRandom\
                                3: HillClimbing\
                                4: Simmulated Annealing'))
    visualizerChoice = int(input('What visualizer do you want?\
                                 1: Normal visualizer\
                                 2: Bulk visualizer'))
    isEmpty = True
    fhAmount = 0
    bAmount = 0
    mAmount = 0
    if gridChoice == 1:
        fileName = str(input('Please give me a file name: '))
        area = DataHelper(fileName).getArea()
        isEmpty = False
    else:
        area = Area()
        amountChoice = int(input('How many houses do you want? \
                                  1: 20\
                                  2: 40\
                                  3: 60'))
        if amountChoice == 1:
            fhAmount = 12
            bAmount = 5
            mAmount = 3
        elif amountChoice == 2:
            fhAmount = 24
            bAmount = 10
            mAmount = 6
        elif amountChoice == 3:
            fhAmount = 36
            bAmount = 15
            mAmount = 9

    if algorithmChoice == 1:
        algorithm = RandomAlgorithm(area, fhAmount,
                                    bAmount, mAmount, isEmpty)
    elif algorithmChoice == 2:
        algorithm = SpeedRandomAlgorithm(area, fhAmount,
                                         bAmount, mAmount, isEmpty)
    elif algorithmChoice == 3:
        algorithm = HillClimbingAlgorithm(area, fhAmount,
                                          bAmount, mAmount, isEmpty)
    elif algorithmChoice == 4:
        # SIMMULATED ANNEALING
        pass

    if visualizerChoice == 1:
        visualizer = Visualizer(area, algorithm)
    elif visualizerChoice == 2:
        runs = int(input('How many runs do you want to do? '))
        visualizer = BulkVisualizer(area, algorithm, runs)

    visualizer.on_execute()


if __name__ == "__main__":
    main()
