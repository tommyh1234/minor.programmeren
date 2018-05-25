from objects.familyHome import FamilyHome
from objects.bungalow import Bungalow
from objects.mansion import Mansion


def construction_list(area, fhAmount, bAmount, mAmount):
    """Generate a list of houses to be placed

    Keyword arguments:
    area        -- the area to fill
    fhAmount    -- the amount of family homes
    bAmount     -- the amount of bungalows
    mAmount     -- the amount of mansions
    """

    # create a list with the required amount of houses
    houses = []
    for k in range(0, mAmount):
        houses.append(Mansion(area))
    for j in range(0, bAmount):
        houses.append(Bungalow(area))
    for i in range(0, fhAmount):
        houses.append(FamilyHome(area))

    return houses
