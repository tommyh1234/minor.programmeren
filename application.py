from objects.map import Map
from objects.mansion import Mansion

def main():
    grid = Map()

    mansion = Mansion()
    grid.place_house(mansion, 5, 5)
