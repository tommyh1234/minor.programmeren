from objects.water import Water
import random
import math


def water_list(area, waterAmount):

    # determine size of water areas
    surfaceoToFlood = area.surface() * 0.2
    surfaceoLeftToFlood = surfaceoToFlood
    waterSurface = 0

    # create list with required amount of water areas,
    waters = []
    for i in range(0, waterAmount - 1):
        currentWater = Water(area)
        # choose dimensions between 1 and square root of area to flood
        prospectiveWidth = random.randint(1, int(math.sqrt(surfaceoToFlood)))
        prospectiveHeight = random.randint(1, int(math.sqrt(surfaceoToFlood)))
        prospectiveRatio = prospectiveWidth / prospectiveHeight

        # check for max. aspect ratio of 1:4 || 4:1
        # in width:height || height:width
        while (prospectiveRatio < 1/4 or prospectiveRatio > 4):
            prospectiveWidth = random.randint(1,
                                              int(math.sqrt(surfaceoToFlood)))
            prospectiveHeight = random.randint(1,
                                               int(math.sqrt(surfaceoToFlood)))
            prospectiveRatio = prospectiveWidth / prospectiveHeight

        # set dimensions if they pass ratio test
        currentWater.width = prospectiveWidth
        currentWater.height = prospectiveHeight
        waters.append(currentWater)
        waterSurface = currentWater.width * currentWater.height
        surfaceoLeftToFlood = surfaceoToFlood - waterSurface

    # for last water area take as dimensions what's left of surface to flood
    currentWater = Water(area)
    currentWater.width = math.ceil(math.sqrt(surfaceoToFlood))
    currentWater.height = math.ceil(math.sqrt(surfaceoToFlood))
    waters.append(currentWater)
    waterSurface = currentWater.width * currentWater.height
    surfaceoLeftToFlood = surfaceoToFlood - waterSurface

    print("Flooded {}m2 with {} water area(s)".format(surfaceoToFlood / 4, waterAmount))

    return waters
