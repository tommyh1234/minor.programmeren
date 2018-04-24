from objects.area import Area
from objects.familyHome import FamilyHome
from objects.bungalow import Bungalow
from objects.mansion import Mansion

def main():
    grid = Area()

    familyHome = FamilyHome(grid)
    bungalow = Bungalow(grid)
    mansion = Mansion(grid)
    
    grid.place_house(mansion, 5, 5)