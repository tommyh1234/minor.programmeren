from objects.area import Area
# from algorithms.speedrandom import SpeedRandomAlgorithm
from algorithms.hillClimbing import HillClimbingAlgorithm
# from algorithms.randomalg import RandomAlgorithm
from bulkvisualizer import BulkVisualizer
from algorithms.hillClimbing import HillClimbingAlgorithm 
from algorithms.simulatedannealing import simulatedAnnealing

def main():

    lowestTemp = None
    highestTemp = None
    typeOfSimulatedAnnealing = None
    totalIteration = int(input("how many interation?: "))

    hillClimbingOrSimulatedAnnealing = int(input( 
                                            "------------------------------------\n"
                                            "1 = HillClimbing\n"
                                            "2 = Simulated Annealing\n"
                                            "Type number for algorithm: "))

    if hillClimbingOrSimulatedAnnealing == 2:
        beginLength = input("------------------------------------\n"
                           "What is the begin length? ")

        endLength = input("------------------------------------\n"
                            "What is the end length? ")

        beginTemp = input("------------------------------------\n"
                           "What is the begin temperature? ")

        endTemp = input("------------------------------------\n"
                            "What is the end temperature? ")

        typeOfSimulatedAnnealing = input("------------------------------------\n"
                                         "1 = Lineair\n" 
                                         "2 = Exponential\n" 
                                         "3 = Sigmoidal \n" 
                                         "What type of simulated annealing?: ")

    # # just Random algorithm
    # grid = Area()
    algorithm = HillClimbingAlgorithm(self,\
                                      area,\
                                      fhAmount,\
                                      bAmount,\
                                      mAmount,\
                                      isEmpty,\
                                      beginTemp,\
                                      endTemp,\
                                      totalIteration,\
                                      currentIteration)
                           
    # # algorithm = RandomAlgorithm(grid, 36, 15, 9, totalIteration)       
    # # #                                                  # 20h: 12, 5, 3
    # # #                                                  # 40: 24, 10, 6
    # # #                                                  # 60: 36, 15, 9
    # visualizer = BulkVisualizer(grid, algorithm, 1)
    # visualizer.on_execute()

    # # # just SpeedRandom Algorithm
    # # grid = Area()
    # # algorithm = SpeedRandomAlgorithm(grid, 36, 15, 9, totalIteration)  
    # # #                                                  # 20h: 12, 5, 3
    # # #                                                  # 40: 24, 10, 6
    # # #                                                  # 60: 36, 15, 9
    # # visualizer = BulkVisualizer(grid, algorithm, 10)
    # # visualizer.on_execute()

    # #   just a HillClimbing algorithm
    # # grid = Area()
    # # TODO: notice that hillclimbingAlgorithm has fourth value
    # # for total amound of itteration.
    # # algorithm = HillClimbingAlgorithm(grid, 36, 15, 9, totalIteration)  
    # # #                                                   # 20h: 12, 5, 3
    # # #                                                   # 40: 24, 10, 6
    # # #                                                   # 60: 36, 15, 9
    # # visualizer = BulkVisualizer(grid, algorithm, 10)
    # # visualizer.on_execute()


if __name__ == "__main__":
    main()
