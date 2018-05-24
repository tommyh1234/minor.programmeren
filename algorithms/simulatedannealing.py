from algorithms.algorithm import Algorithm
from algorithms.hillClimbing import HillClimbingAlgorithm 
from random import random

class simulatedAnnealing(Algorithm):
	def __init__(self, currentPrice,\
                       originalPrice,\
                       endTemp,\
                       typeOfSimulatedAnnealing,\
                       totalIteration,\
                       currentIteration):

		self.currentPrice = currenTemp
		self.originalPrice = originalPrice
		self.beginTemp = beginTemp
		self.endTemp = endTemp
		self.typeOfSimulatedAnnealing = typeOfSimulatedAnnealing		
		self.totalIteration = totalIteration
		self.currentIteration = currentIteration

		# Lineair 
		if typeOfSimulatedAnnealing == 1:
				self.currenTemp = (beginTemp - currentIteration * 
								  (beginTemp - endTemp) / totalIteration)

		# Exponential
		if typeOfSimulatedAnnealing == 2:
				self.currenTemp = (beginTemp * (endTemp/beginTemp) ^ 
								   (currentIteration / totalIteration))

		# Sigmoidal
		if typeOfSimulatedAnnealing == 3:
				self.currenTemp = (endTemp + (beginTemp + endTemp) / 
				(1 + exp(0.3 (currentIteration - totalIteration / 2))))	

		shortening = (currentPrice - originalPrice) / originalPrice
		coolingscheme = shortening / currenTemp
		acceptationChange = exp(coolingscheme)

		currentIteration += 1

		if acceptationChange < random.random():
			return False
