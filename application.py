from objects.area import Area

from algorithms.speedrandom import SpeedRandomAlgorithm
from algorithms.hillClimbing import HillClimbingAlgorithm
from algorithms.randomalg import RandomAlgorithm

from visualizer import Visualizer
from bulkvisualizer import BulkVisualizer
# from datahelper import DataHelper


def main():
    print("WELCOME TO AMSTELHAEGE")
    gridChoice = int(input('Do you want to load in a grid or start from scratch?\n\
 1: Load a grid\n 2: Start from scratch\n'))
    algorithmChoice = int(input('What algorithm do you want to run?\n \
 1: Random \n 2: SpeedRandom\n 3: HillClimbing\n 4: Simmulated Annealing\n'))
    visualizerChoice = int(input('What visualizer do you want?\n \
 1: Normal visualizer\n 2: Bulk visualizer\n'))
    isEmpty = True
    fhAmount = 0
    bAmount = 0
    mAmount = 0
    if gridChoice == 1:
        fileName = str(input('Please give me a file name: \n'))
        area = DataHelper(fileName).getArea()
        isEmpty = False
    else:
        area = Area()
        amountChoice = int(input('How many houses do you want? \n\
 1: 20\n 2: 40\n 3: 60\n'))
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
        runs = int(input('How many runs do you want to do? \n'))
        visualizer = BulkVisualizer(area, algorithm, runs)

    visualizer.on_execute()


if __name__ == "__main__":
    main()
