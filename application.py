from objects.area import Area

from algorithms.algorithm import Algorithm
from algorithms.speedrandom import SpeedRandomAlgorithm
from algorithms.hillClimbing import HillClimbingAlgorithm
from algorithms.randomalg import RandomAlgorithm
from algorithms.greedy import GreedyAlgorithm

from visualizers.visualizer import Visualizer
from visualizers.bulkvisualizer import BulkVisualizer
from visualizers.nodrawvisualizer import NoDrawVisualizer
from visualizers.nodrawbulkvisualizer import NoDrawBulkVisualizer

from datahelper import DataHelper


def main():
    """Present the user with choices about the algorithm to run"""

    print("----------------------")
    print("WELCOME TO AMSTELHAEGE \n")

    # let the user choose a new or existing grid
    gridChoice = int(input('Do you want to load in a grid '
                           'or start from scratch?\n'
                           '1: Load a grid\n'
                           '2: Start from scratch\n'
                           'Your choice: '))
    print("")

    # let the user choose an algorithm
    algorithmChoice = int(input('What algorithm do you want to run?\n'
                                '1: Random \n'
                                '2: Greedy \n'
                                '3: SpeedRandom\n'
                                '4: HillClimbing\n'
                                '5: Simmulated Annealing\n'
                                '6: Do Nothing (show only)'
                                'Your choice: '))
    if algorithmChoice == 4 or algorithmChoice == 5:
        print("")
        totalIterations = int(input('How many steps should algorithm make?\n'
                                    'Your choice: '))
        if algorithmChoice == 5:
            print("")
            typeOfSimulatedAnnealing = int(input('What type of Simulated'
                                                 ' Annealing?\n'
                                                 '1: lineair \n'
                                                 '2: exponential\n'
                                                 '3: sigmoidal\n'
                                                 'Your choice: '))
        if algorithmChoice == 5:
            print("")
            beginTemp = int(input('What is the begin temperature?\n'
                                  'Your choice: '))
            print("")
            endTemp = int(input('What is the end temperature?\n'
                                'Your choice: '))
            print("")
            correctionShortening = int(input('What correction factor for'
                                             ' shortening the would you like'
                                             ' to use?\n'
                                             ' Your choice: '))
    print("")

    # let the user choose a type of visualization.
    # Normal visualizer renders a single visualisation
    # Bulk visualizer can render several maps after one another
    visualizerChoice = int(input('What visualizer do you want?\n'
                                 '1: Normal visualizer\n'
                                 '2: Bulk visualizer\n'
                                 '3: No-draw normal visualizer\n'
                                 '4: No-draw bulk visualizer\n'
                                 'Your choice: '))
    print("")
    isEmpty = True
    fhAmount = 0
    bAmount = 0
    mAmount = 0

    if gridChoice == 1:
        # ask the user for the file where the existing grid is stored
        fileName = str(input('Please provide a file name: \n'
                             'Your choice: '))
        area = DataHelper(fileName).getArea()
        isEmpty = False
    else:
        # or create a new grid
        area = Area()
        houseAmountChoice = int(input('How many houses do you want? \n'
                                      '1: 20\n'
                                      '2: 40\n'
                                      '3: 60\n'
                                      'Your choice: '))
        print("")
        # set the correct ratio of house types
        # for different amounts of houses
        if houseAmountChoice == 1:
            fhAmount = 12
            bAmount = 5
            mAmount = 3
        elif houseAmountChoice == 2:
            fhAmount = 24
            bAmount = 10
            mAmount = 6
        elif houseAmountChoice == 3:
            fhAmount = 36
            bAmount = 15
            mAmount = 9

    # if applicable for the algorithm chosen, provide further choices
    if algorithmChoice != 2:
        placementOrder = int(input('In what order do you want houses '
                                   'to be placed on the map?\n'
                                   '1: Random \n'
                                   '2: First Mansions, then Bungalows, '
                                   'then Family homes \n'
                                   'Your choice: '))
        print("")
        waterAmountChoice = int(input('How many water areas'
                                      ' do you want on the map? \n'
                                      '1: 1 Area \n'
                                      '2: 2 Area\'s \n'
                                      '3: 3 Area\'s \n'
                                      '4: 4 Area\'s \n'
                                      '5: Random amount of Area\'s \n'
                                      'Your choice: '))
        if waterAmountChoice == "5":
            waterAmountChoice = "Random"
        print("")

    # initiate the algorithm chosen by the user
    if algorithmChoice == 1:
        algorithm = RandomAlgorithm(area, fhAmount,
                                    bAmount, mAmount,
                                    placementOrder, waterAmountChoice,
                                    isEmpty)
    elif algorithmChoice == 2:
        algorithm = GreedyAlgorithm(area, fhAmount,
                                    bAmount, mAmount, isEmpty)
    elif algorithmChoice == 3:
        algorithm = SpeedRandomAlgorithm(area, fhAmount,
                                         bAmount, mAmount,
                                         placementOrder, waterAmountChoice,
                                         isEmpty)
    elif algorithmChoice == 4:
        algorithm = HillClimbingAlgorithm(area, fhAmount,
                                          bAmount, mAmount,
                                          placementOrder, waterAmountChoice,
                                          isEmpty, totalIterations)
    elif algorithmChoice == 5:
        algorithm = HillClimbingAlgorithm(area, fhAmount,
                                          bAmount, mAmount, placementOrder,
                                          waterAmountChoice,
                                          isEmpty, totalIterations,
                                          beginTemp, endTemp,
                                          typeOfSimulatedAnnealing,
                                          correctionShortening)

    elif algorithmChoice == 6:
        algorithm = Algorithm(area, fhAmount,
                              bAmount, mAmount,
                              isEmpty)

    # initiate the visualization requested by the user
    if visualizerChoice == 1:
        # enable downward graphing
        if algorithmChoice == 5:
            visualizer = Visualizer(area, algorithm, True)
        else:
            visualizer = Visualizer(area, algorithm, True)
    elif visualizerChoice == 2:
        runs = int(input('How many runs do you want to do? \n'
                         'Your choice: '))
        visualizer = BulkVisualizer(area, algorithm, runs)
    elif visualizerChoice == 3:
        visualizer = NoDrawVisualizer(area, algorithm)
    elif visualizerChoice == 4:
        runs = int(input('How many runs do you wnat to do? \n'
                         'Your choice: '))
        visualizer = NoDrawBulkVisualizer(area, algorithm, runs)

    # notify the user of the end of the menu
    print("Starting your Algorithm...")
    print("----------------------")
    visualizer.on_execute()

    # # # just SpeedRandom Algorithm
    # # grid = Area()
    # # algorithm = SpeedRandomAlgorithm(grid, 36, 15, 9, totalIterations)
    # # #                                                  # 20h: 12, 5, 3
    # # #                                                  # 40: 24, 10, 6
    # # #                                                  # 60: 36, 15, 9
    # # visualizer = BulkVisualizer(grid, algorithm, 10)
    # # visualizer.on_execute()

    # #   just a HillClimbing algorithm
    # # grid = Area()
    # # TODO: notice that hillclimbingAlgorithm has fourth value
    # # for total amound of itteration.
    # # algorithm = HillClimbingAlgorithm(grid, 36, 15, 9, totalIterations)
    # # #                                                   # 20h: 12, 5, 3
    # # #                                                   # 40: 24, 10, 6
    # # #                                                   # 60: 36, 15, 9
    # # visualizer = BulkVisualizer(grid, algorithm, 10)
    # # visualizer.on_execute()


if __name__ == "__main__":
    main()
