from objects.familyHome import FamilyHome
from objects.bungalow import Bungalow
from objects.mansion import Mansion


def construction_list(area, fhAmount, bAmount, mAmount):

    # create a list with the required amount of houses
    houses = []
    for i in range(0, fhAmount):
        houses.append(FamilyHome(area))
    for j in range(0, bAmount):
        houses.append(Bungalow(area))
    for k in range(0, mAmount):
        houses.append(Mansion(area))
    print('All houses: {}'.format(houses))

    return houses

