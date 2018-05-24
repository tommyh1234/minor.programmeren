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
        potentialDimension = int(math.sqrt(surfaceoLeftToFlood))
        prospectiveWidth = random.randint(1, potentialDimension)
        prospectiveHeight = random.randint(1, potentialDimension)
        prospectiveRatio = prospectiveWidth / prospectiveHeight

        # check for max. aspect ratio of 1:4 || 4:1
        # in width:height || height:width
        while (prospectiveRatio < 1/4 or prospectiveRatio > 4):
            potentialDimension = int(math.sqrt(surfaceoLeftToFlood))
            prospectiveWidth = random.randint(1, potentialDimension)
            prospectiveHeight = random.randint(1, potentialDimension)
            prospectiveRatio = prospectiveWidth / prospectiveHeight

        # set dimensions if they pass ratio test
        currentWater.width = prospectiveWidth
        currentWater.height = prospectiveHeight
        waters.append(currentWater)
        waterSurface = currentWater.width * currentWater.height
        surfaceoLeftToFlood = surfaceoLeftToFlood - waterSurface

    # for last water area take as dimensions what's left of surface to flood
    currentWater = Water(area)
    currentWater.width = math.ceil(math.sqrt(surfaceoLeftToFlood))
    currentWater.height = math.ceil(math.sqrt(surfaceoLeftToFlood))
    waters.append(currentWater)
    waterSurface = currentWater.width * currentWater.height
    surfaceoLeftToFlood = surfaceoLeftToFlood - waterSurface

    print("Flooded {}m2 (20% of the map) with {} water area(s)"
          .format(surfaceoToFlood / 4, waterAmount))

    return waters
