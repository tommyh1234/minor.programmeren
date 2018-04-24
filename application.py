from objects.area import Area
from objects.familyHome import FamilyHome
from objects.bungalow import Bungalow
from objects.mansion import Mansion

def main():
	amount = 0

	while amount != 20 or amount != 40 or amount != 60:
		amount = raw_input("20, 40 or 60 houses?: ")
			print("Amount houses not 20, 40 or 60")
    
    grid = Area(amount)

    familyHome = FamilyHome(grid)
    bungalow = Bungalow(grid)
    mansion = Mansion(grid)
    
    grid.place_house(mansion, 5, 5)