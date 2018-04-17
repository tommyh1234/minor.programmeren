from objects.area import Area
from objects.mansion import Mansion


def main():
    grid = Area()

    mansion = Mansion(2)
    grid.place_house(mansion, 5, 5)
