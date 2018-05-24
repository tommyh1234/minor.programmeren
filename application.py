from objects.area import Area
from algorithms.speedrandom import SpeedRandomAlgorithm
from algorithms.hillClimbing import HillClimbingAlgorithm
from algorithms.randomalg import RandomAlgorithm
from algorithms.greedy import GreedyAlgorithm
from visualizer import Visualizer
from bulkvisualizer import BulkVisualizer
from datahelper import DataHelper


def main():
    print("----------------------")
    print("WELCOME TO AMSTELHAEGE \n")
    gridChoice = int(input('Do you want to load in a grid '
                           'or start from scratch?\n'
                           '1: Load a grid\n'
                           '2: Start from scratch\n'
                           'Your choice: '))
    print("")
    algorithmChoice = int(input('What algorithm do you want to run?\n'
                                '1: Random \n'
                                '2: Greedy \n'
                                '3: SpeedRandom\n'
                                '4: HillClimbing\n'
                                '5: Simmulated Annealing\n'
                                'Your choice: '))
    print("")
    visualizerChoice = int(input('What visualizer do you want?\n'
                                 '1: Normal visualizer\n'
                                 '2: Bulk visualizer\n'
                                 'Your choice: '))
    print("")
    isEmpty = True
    fhAmount = 0
    bAmount = 0
    mAmount = 0
    if gridChoice == 1:
        fileName = str(input('Please give me a file name: \n'
                             'Your choice: '))
        area = DataHelper(fileName).getArea()
        isEmpty = False
    else:
        area = Area()
        amountChoice = int(input('How many houses do you want? \n'
                                 '1: 20\n'
                                 '2: 40\n'
                                 '3: 60\n'
                                 'Your choice: '))
        print("")
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

    if algorithmChoice != 2:
        placementOrder = int(input('In what order do you want houses '
                                   'to be placed on the map?\n'
                                   '1: Random \n'
                                   '2: Mansions > Bungalows > Family homes \n'
                                   'Your choice: '))
        print("")
        waterAmountChoise = int(input('How many water areas do you want on the map? \n'
                                      '1: 1 Area \n'
                                      '2: 2 Area\'s \n'
                                      '3: 3 Area\'s \n'
                                      '4: 4 Area\'s \n'
                                      '5: Random amount of Area\'s \n'
                                      'Your choice: '))
        if waterAmountChoise == "5":
            waterAmountChoise = "Random"
        print("")

    if algorithmChoice == 1:
        algorithm = RandomAlgorithm(area, fhAmount,
                                    bAmount, mAmount,
                                    placementOrder, waterAmountChoise,
                                    isEmpty)
    elif algorithmChoice == 2:
        algorithm = GreedyAlgorithm(area, fhAmount,
                                    bAmount, mAmount, isEmpty)
    elif algorithmChoice == 3:
        algorithm = SpeedRandomAlgorithm(area, fhAmount,
                                         bAmount, mAmount,
                                         placementOrder, waterAmountChoise,
                                         isEmpty)
    elif algorithmChoice == 4:
        algorithm = HillClimbingAlgorithm(area, fhAmount,
                                          bAmount, mAmount,
                                          placementOrder, waterAmountChoise,
                                          isEmpty)
    elif algorithmChoice == 5:
        # SIMMULATED ANNEALING
        pass

    if visualizerChoice == 1:
        visualizer = Visualizer(area, algorithm)
    elif visualizerChoice == 2:
        runs = int(input('How many runs do you want to do? \n'
                         'Your choice: '))
        visualizer = BulkVisualizer(area, algorithm, runs)

    print("Starting your Algorithm...")
    print("----------------------")
    visualizer.on_execute()


if __name__ == "__main__":
    main()
