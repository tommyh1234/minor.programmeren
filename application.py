from objects.area import Area
from objects.familyHome import FamilyHome
from objects.bungalow import Bungalow
from objects.mansion import Mansion
from algorithms.randomalg import fillRandomGrid

def main():
    grid0 = Area()
    fillRandomGrid(grid0, 36, 15, 9)

if __name__ == "__main__":
    main()
