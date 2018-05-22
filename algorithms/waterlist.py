from objects.water import Water
import random
import math


def water_list(area, waterAmount):

    # determine size of water areas
    surfaceoToFlood = area.surface() * 0.2
    waterSurface = 0
    print("waterAmount:", waterAmount)
    print("Tot. surface to flood: {} * 0.5 m2".format(surfaceoToFlood))

    # create list with required amount of water areas,
    waters = []
    for i in range(0, waterAmount - 1):
        currentWater = Water(area)
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
            prospectiveSurface = prospectiveWidth * prospectiveHeight
            print("prosWidth: {}, prosHeight: {}, prosSurface: {}"
                  .format(prospectiveWidth,
                          prospectiveHeight,
                          prospectiveSurface))

        currentWater.width = prospectiveWidth
        currentWater.height = prospectiveHeight
        waters.append(currentWater)
        waterSurface = currentWater.width * currentWater.height
        surfaceoToFlood = surfaceoToFlood - waterSurface
        print("defWidth: {}, defHeight: {}, defSurface: {}, surfaceToFlood: {}"
              .format(currentWater.width,
                      currentWater.height,
                      waterSurface,
                      surfaceoToFlood))
        print("---Create--Next--Water--Area----")

    # for last water area take as dimensions what's left
    currentWater = Water(area)
    currentWater.width = math.ceil(math.sqrt(surfaceoToFlood))
    currentWater.height = math.ceil(math.sqrt(surfaceoToFlood))
    waters.append(currentWater)
    waterSurface = currentWater.width * currentWater.height
    surfaceoToFlood = surfaceoToFlood - waterSurface
    print("defWidth: {}, defHeight: {}, defSurface: {}, surfaceToFlood: {}"
          .format(currentWater.width,
                  currentWater.height,
                  waterSurface,
                  surfaceoToFlood))

    print(waters)
    print("---All--Water--Areas--Created---")

    return waters
